#!/usr/bin/env python3
"""Rebuild xs-writer skill field files from xs-helper source of truth (v3).

Usage:
    python rebuild_fields.py [--xs-helper-dir PATH]

Default xs-helper path: ~/.cache/xs-helper/xs-helper backup/
This matches the path used by sync.sh.
"""

import os
import re
import sys
import argparse

DEFAULT_XS_HELPER = os.path.join(os.path.expanduser('~'), '.cache', 'xs-helper', 'xs-helper backup')
SKILL_BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fields')


def parse_field_md(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    info = {}
    basename = os.path.basename(filepath).replace('.md', '')
    # Convert underscore-wrapped text to parentheses: _abc_ -> (abc)
    field_name = re.sub(r'_([^_]+)_', r'(\1)', basename)
    info['name'] = field_name

    is_chinese_name = bool(re.search(r'[\u4e00-\u9fff]', field_name))

    # Extract ALL values inside GetField("...") and GetQuote("...")
    # Match both GetField("X") and GetField("X",param:=...) patterns
    all_codes = re.findall(r'(?:GetField|GetQuote)\("([^"]+)"', content)

    # Also check q_xxx shorthand
    q_codes = re.findall(r'q_(\w+)', content)

    # Filter: find the English code (not the Chinese field name)
    eng_code = ''

    if is_chinese_name:
        # For Chinese-named fields, find non-Chinese aliases
        for code in all_codes:
            if code != field_name and not re.match(r'^[\u4e00-\u9fff]', code):
                eng_code = code
                break
        # Fallback to q_ shorthand
        if not eng_code and q_codes:
            eng_code = q_codes[0]
    else:
        # For English-named fields (Delta, Gamma, etc.), field name IS the code
        # But check if there's a different English alias too
        other_codes = [c for c in all_codes if c != field_name and not re.match(r'^[\u4e00-\u9fff]', c)]
        if other_codes:
            eng_code = other_codes[0]
        else:
            eng_code = field_name

    info['english'] = eng_code

    # Extract 支援商品
    product_match = re.search(r'支援商品\s*\|\s*(.+)', content)
    info['products'] = product_match.group(1).strip() if product_match else ''

    # Extract first sentence of description
    desc_match = re.search(r'## 說明\s*\n\s*\n(.+?)(?:\n|$)', content)
    info['description'] = desc_match.group(1).strip()[:40] if desc_match else ''

    return info


def get_fields_from_dir(dirpath):
    fields = []
    if not os.path.exists(dirpath):
        return fields
    for fname in sorted(os.listdir(dirpath)):
        if fname.endswith('.md'):
            fpath = os.path.join(dirpath, fname)
            try:
                info = parse_field_md(fpath)
                fields.append(info)
            except Exception as e:
                print(f"  Warning: {fpath}: {e}", file=sys.stderr)
    return fields


def generate_table(fields):
    lines = []
    lines.append("| 欄位名稱 | English Code | 支援商品 | 備註 |")
    lines.append("|----------|-------------|---------|------|")
    for f in fields:
        eng = f['english'] if f['english'] else '—'
        lines.append(f"| {f['name']} | {eng} | {f['products']} | {f['description']} |")
    return '\n'.join(lines)


def write_file(category, filename, content):
    filepath = os.path.join(SKILL_BASE, category, f'{filename}.md')
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    field_count = sum(1 for line in content.split('\n') if line.startswith('|') and not line.startswith('| 欄位') and not line.startswith('|--'))
    no_eng = sum(1 for line in content.split('\n') if '| — |' in line)
    print(f"  {category}/{filename}.md -> {field_count} fields ({no_eng} without English code)")


def build_file(category, dir_name, filename, title, desc, example_code, xs_helper_base):
    dirpath = os.path.join(xs_helper_base, dir_name)
    fields = get_fields_from_dir(dirpath)
    table = generate_table(fields)
    content = f"# {title} ({len(fields)})\n\n> {desc}\n\n{table}\n\n## 使用範例\n\n```xs\n{example_code}```\n\n> 欄位名稱以 xs-helper 官方文件為準\n"
    write_file(category, filename, content)
    return fields


def build_chips_files(category, base_dir, chip_configs, xs_helper_base):
    chips_dir = os.path.join(xs_helper_base, base_dir, "籌碼")
    all_chips = get_fields_from_dir(chips_dir)

    for file_key, config in chip_configs.items():
        title = config['title']
        desc = config['desc']
        keywords = config['keywords']
        example = config['example']
        is_default = config.get('is_default', False)

        if is_default:
            other_keywords = []
            for k, c in chip_configs.items():
                if k != file_key:
                    other_keywords.extend(c['keywords'])
            fields = [f for f in all_chips if not any(kw in f['name'] for kw in other_keywords)]
        else:
            fields = [f for f in all_chips if any(kw in f['name'] for kw in keywords)]

        table = generate_table(fields)
        content = f"# {title} ({len(fields)})\n\n> {desc}\n\n{table}\n\n## 使用範例\n\n```xs\n{example}```\n\n> 欄位名稱以 xs-helper 官方文件為準\n"
        write_file(category, file_key, content)


def build_finance_files(base_dir, xs_helper_base):
    finance_dir = os.path.join(xs_helper_base, base_dir, "財務")
    all_finance = get_fields_from_dir(finance_dir)

    balance_kw = ['資產', '負債', '股東權益', '流動', '速動', '淨值', '股本', '公積', '庫藏股票', '應付', '應收', '存貨', '短期借', '長期', '無形', '退休金', '遞延', '預付', '預收', '合約負債', '加權平均', '總流通', '外幣換算', '未完工程', '每股流動淨資產', '或有負債', '商業本票', '一年內到期', '借款依存', '未分配盈餘', '背書保證', '資金貸放']
    cashflow_kw = ['現金流', '現金再投資', '現金及約當', '自由現金', '資本支出', '理財活動', '投資活動', '來自營運', '現金派息', '營運資金']
    profit_kw = ['ROE', 'ROA', 'ROIC', '淨利率', '毛利率', '營業利益率', '稅前淨利率', '稅後淨利率', '杜邦', '報酬率', '每股稅', '每股盈餘', '每股營業利益', '稀釋', '常續性', '經常利益', '停業部門', '稅前息前', '本期稅後', '所得稅', '有效稅率', '每股淨值', '誠信指標', '因子', '盈餘', 'EPS']

    def classify(name):
        for kw in cashflow_kw:
            if kw in name:
                return 'cashflow'
        for kw in profit_kw:
            if kw in name:
                return 'profitability'
        for kw in balance_kw:
            if kw in name:
                return 'balance'
        return 'revenue'

    groups = {'balance': [], 'cashflow': [], 'profitability': [], 'revenue': []}
    for f in all_finance:
        groups[classify(f['name'])].append(f)

    configs = {
        'finance-balance': ('Selection 財務-資產負債欄位', '用於選股腳本\n> 資產負債表相關欄位、財務比率', 'balance',
            'cr = GetField("流動比率");\ndr = GetField("負債比率");\nif cr > 150 and dr < 50 then ret = 1;\n'),
        'finance-cashflow': ('Selection 財務-現金流欄位', '用於選股腳本\n> 現金流量表相關欄位', 'cashflow',
            'fcf = GetField("自由現金流量");\nif fcf > 0 then ret = 1;\n'),
        'finance-profitability': ('Selection 財務-獲利能力欄位', '用於選股腳本\n> 獲利能力、每股數據、成長率等', 'profitability',
            'roe = GetField("股東權益報酬率");\neps = GetField("每股稅後淨利(元)");\nif roe > 15 and eps > 2 then ret = 1;\n'),
        'finance-revenue': ('Selection 財務-營收/費用欄位', '用於選股腳本\n> 營收、成本、費用、週轉率等', 'revenue',
            'growth = GetField("營收成長率");\nmargin = GetField("營業毛利率");\nif growth > 20 and margin > 30 then ret = 1;\n'),
    }

    for file_key, (title, desc, group_key, example) in configs.items():
        fields = groups[group_key]
        table = generate_table(fields)
        content = f"# {title} ({len(fields)})\n\n> {desc}\n\n{table}\n\n## 使用範例\n\n```xs\n{example}```\n\n> 欄位名稱以 xs-helper 官方文件為準\n"
        write_file('selection', file_key, content)


def main():
    parser = argparse.ArgumentParser(description='Rebuild xs-writer field files from xs-helper')
    parser.add_argument('--xs-helper-dir', default=DEFAULT_XS_HELPER,
                        help=f'Path to xs-helper backup directory (default: {DEFAULT_XS_HELPER})')
    args = parser.parse_args()

    xs_helper_base = args.xs_helper_dir

    if not os.path.exists(xs_helper_base):
        print(f"ERROR: xs-helper directory not found: {xs_helper_base}")
        print("Run sync.sh first to clone the xs-helper repo.")
        sys.exit(1)

    print(f"Source: {xs_helper_base}")
    print(f"Target: {SKILL_BASE}")
    print()

    print("=== Building Quote Fields ===")
    build_file('quote', '報價欄位/常用', 'common', 'Quote 常用欄位',
        '用於 `GetQuote("欄位名")` 即時報價',
        'value1 = GetQuote("成交");  // 或 GetQuote("Last")\nvalue2 = GetQuote("總量(日)");  // 或 GetQuote("DailyVolume")\n',
        xs_helper_base)

    build_file('quote', '報價欄位/價格', 'price', 'Quote 價格欄位',
        '用於 `GetQuote("欄位名")` 即時報價',
        'high = GetQuote("最高(日)");  // 或 GetQuote("DailyHigh")\nlow = GetQuote("最低(日)");  // 或 GetQuote("DailyLow")\nspread = high - low;\n',
        xs_helper_base)

    build_file('quote', '報價欄位/量能', 'volume', 'Quote 量能欄位',
        '用於 `GetQuote("欄位名")` 即時報價',
        'vol = GetQuote("總量(日)");  // 或 GetQuote("DailyVolume")\nyestVol = GetQuote("昨量");  // 或 GetQuote("PreTotalVolume")\nratio = vol / yestVol;\n',
        xs_helper_base)

    build_file('quote', '報價欄位/五檔統計', 'level2', 'Quote 五檔統計欄位',
        '用於 `GetQuote("欄位名")` 即時報價\n> 五檔統計：買進1~5 為委買價格，委買1~5 為委買量；賣出1~5 為委賣價格，委賣1~5 為委賣量',
        'bid1 = GetQuote("買進1");  // 或 GetQuote("BestBid1") 第一檔買進價\nask1 = GetQuote("賣出1");  // 或 GetQuote("BestAsk1") 第一檔賣出價\nbidSize1 = GetQuote("委買1");  // 或 GetQuote("BestBidSize1") 第一檔委買量\naskSize1 = GetQuote("委賣1");  // 或 GetQuote("BestAskSize1") 第一檔委賣量\n',
        xs_helper_base)

    build_file('quote', '報價欄位/市場統計', 'market-stats', 'Quote 市場統計欄位',
        '用於 `GetQuote("欄位名")` 即時報價\n> 適用於大盤指數商品',
        'up = GetQuote("上漲家數");\ndown = GetQuote("下跌家數");\n',
        xs_helper_base)

    build_file('quote', '報價欄位/財務', 'finance', 'Quote 財務欄位',
        '用於 `GetQuote("欄位名")` 即時報價\n> 取得最新一期財報數據',
        'eps = GetQuote("每股盈餘");  // 或 GetQuote("CurrentEPS")\nroe = GetQuote("股東權益報酬率");  // 或 GetQuote("CurrentROE")\nopm = GetQuote("營益率");  // 或 GetQuote("OpeProfitMarginRate")\n',
        xs_helper_base)

    build_file('quote', '報價欄位/期權', 'options', 'Quote 期權欄位',
        '用於 `GetQuote("欄位名")` 即時報價\n> 適用於期貨、選擇權商品',
        'delta = GetQuote("Delta");\niv = GetQuote("波動率");  // 或 GetQuote("Volatility")\n',
        xs_helper_base)

    print("\n=== Building Data Fields ===")
    build_file('data', '資料欄位/常用', 'common', 'Data 常用欄位',
        '用於 `GetField("欄位名")` 歷史資料',
        'value1 = GetField("收盤價");  // 或 GetField("Close")\nvalue2 = GetField("成交量");  // 或 GetField("Volume")\n',
        xs_helper_base)

    build_file('data', '資料欄位/價格', 'price', 'Data 價格欄位',
        '用於 `GetField("欄位名")` 歷史資料',
        'avg = GetField("均價");  // 或 GetField("AvgPrice")\nref = GetField("參考價");\n',
        xs_helper_base)

    build_file('data', '資料欄位/量能', 'volume', 'Data 量能欄位',
        '用於 `GetField("欄位名")` 歷史資料',
        'vol = GetField("成交量");  // 或 GetField("Volume")\namt = GetField("成交金額(元)");  // 或 GetField("TradeValue")\n',
        xs_helper_base)

    build_file('data', '資料欄位/基本', 'basic', 'Data 基本欄位',
        '用於 `GetField("欄位名")` 歷史資料',
        'cap = GetField("總市值(元)");  // 或 GetField("TotalMarketValue")\npe = GetField("本益比");  // 或 GetField("PE")\n',
        xs_helper_base)

    build_file('data', '資料欄位/事件', 'events', 'Data 事件欄位',
        '用於 `GetField("欄位名")` 歷史資料',
        'exDate = GetField("除權息日期");  // 或 GetField("ExDividendRightDate")\ndiv = GetField("除息值");  // 或 GetField("ExDividendValue")\n',
        xs_helper_base)

    build_file('data', '資料欄位/市場統計', 'market-stats', 'Data 市場統計欄位',
        '用於 `GetField("欄位名")` 歷史資料\n> 適用於大盤指數商品',
        'up = GetField("上漲家數");\ndown = GetField("下跌家數");\n',
        xs_helper_base)

    build_file('data', '資料欄位/期權', 'options', 'Data 期權欄位',
        '用於 `GetField("欄位名")` 歷史資料\n> 適用於期貨、選擇權商品',
        'oi = GetField("未平倉");\ndelta = GetField("Delta");\n',
        xs_helper_base)

    # Data chips (4 files)
    data_chip_configs = {
        'chips-institutional': {
            'title': 'Data 籌碼-法人欄位',
            'desc': '用於 `GetField("欄位名")` 歷史資料\n> 外資、投信、自營商、法人相關欄位',
            'keywords': ['外資', '投信', '自營商', '法人'],
            'example': 'fBuy = GetField("外資買賣超");  // 或 GetField("Fdifference")\niTrust = GetField("投信買賣超");  // 或 GetField("Sdifference")\ndealer = GetField("自營商買賣超");  // 或 GetField("Ddifference")\n',
        },
        'chips-major': {
            'title': 'Data 籌碼-主力/券商欄位',
            'desc': '用於 `GetField("欄位名")` 歷史資料\n> 主力、控盤者、券商、買賣力等相關欄位',
            'keywords': ['主力', '控盤者', '分公司', '綜合前十大', '官股', '地緣', '關聯', '關鍵', '市場總分點數', '買家數', '賣家數', '買進公司', '賣出公司', '收集派發', '吉尼', '主動'],
            'example': 'major = GetField("主力買賣超張數");  // 或 GetField("LeaderDifference")\ncost = GetField("主力成本");  // 或 GetField("LeaderCost")\n',
        },
        'chips-margin': {
            'title': 'Data 籌碼-融資融券欄位',
            'desc': '用於 `GetField("欄位名")` 歷史資料\n> 融資、融券、券資比等相關欄位',
            'keywords': ['融資', '融券', '券資比', '資券互抵', '還券', '資券比'],
            'example': 'margin = GetField("融資增減張數");  // 或 GetField("Pomnew")\nshort_ = GetField("融券增減張數");  // 或 GetField("Shortsalenew")\n',
        },
        'chips-other': {
            'title': 'Data 籌碼-其他欄位',
            'desc': '用於 `GetField("欄位名")` 歷史資料\n> 散戶、大戶、內部人、董監、借券、庫藏股、當沖、現增等相關欄位',
            'keywords': [],
            'example': 'insider = GetField("內部人持股張數");  // 或 GetField("Insidersharesheld")\nretail = GetField("散戶買賣超張數");  // 或 GetField("Retaildifference")\n',
            'is_default': True,
        },
    }
    build_chips_files('data', '資料欄位', data_chip_configs, xs_helper_base)

    print("\n=== Building Selection Fields ===")
    build_file('selection', '選股欄位/常用', 'common', 'Selection 常用欄位',
        '用於選股腳本 `GetField("欄位名")`',
        'value1 = GetField("收盤價");  // 或 GetField("Close")\nvalue2 = GetField("成交量");  // 或 GetField("Volume")\nif value1 > 50 and value2 > 1000 then ret = 1;\n',
        xs_helper_base)

    build_file('selection', '選股欄位/價格', 'price', 'Selection 價格欄位',
        '用於選股腳本',
        'close = GetField("收盤價");\nhigh = GetField("最高價");\nif close = high then ret = 1;\n',
        xs_helper_base)

    build_file('selection', '選股欄位/量能', 'volume', 'Selection 量能欄位',
        '用於選股腳本',
        'vol = GetField("成交量");\nif vol > 5000 then ret = 1;\n',
        xs_helper_base)

    build_file('selection', '選股欄位/基本', 'basic', 'Selection 基本欄位',
        '用於選股腳本\n> 公司基本資料、股利、市值等',
        'pe = GetField("本益比");\nyield_ = GetField("殖利率");\nif pe < 15 and yield_ > 5 then ret = 1;\n',
        xs_helper_base)

    build_file('selection', '選股欄位/事件', 'events', 'Selection 事件欄位',
        '用於選股腳本\n> 除權息、股東會、增減資等事件日期',
        'exDate = GetField("除權息日期");\nif exDate > 0 then ret = 1;\n',
        xs_helper_base)

    # Selection chips (3 files)
    sel_chip_configs = {
        'chips-institutional': {
            'title': 'Selection 籌碼-法人欄位',
            'desc': '用於選股腳本\n> 外資、投信、自營商、法人相關欄位',
            'keywords': ['外資', '投信', '自營商', '法人'],
            'example': 'fBuy = GetField("外資買賣超");  // 或 GetField("Fdifference")\nif fBuy > 500 then ret = 1;\n',
        },
        'chips-margin': {
            'title': 'Selection 籌碼-融資融券欄位',
            'desc': '用於選股腳本\n> 融資、融券、券資比、週轉率等相關欄位',
            'keywords': ['融資', '融券', '券資比', '資券互抵', '還券', '週轉率', '資券比'],
            'example': 'margin = GetField("融資增減張數");\nif margin < -500 then ret = 1;  // 融資大減\n',
        },
        'chips-major': {
            'title': 'Selection 籌碼-主力/其他欄位',
            'desc': '用於選股腳本\n> 主力、控盤者、散戶、大戶、內部人、董監、借券、庫藏股、當沖等相關欄位',
            'keywords': [],
            'example': 'major = GetField("主力買賣超張數");\nif major > 1000 then ret = 1;\n',
            'is_default': True,
        },
    }
    build_chips_files('selection', '選股欄位', sel_chip_configs, xs_helper_base)

    # Selection finance (4 files)
    build_finance_files('選股欄位', xs_helper_base)

    # Final stats
    print("\n=== Stats ===")
    total_fields = 0
    total_no_eng = 0
    no_eng_list = []
    for root, dirs, files in os.walk(SKILL_BASE):
        for f in sorted(files):
            if f.endswith('.md'):
                fpath = os.path.join(root, f)
                with open(fpath, 'r', encoding='utf-8') as fp:
                    for line in fp:
                        if line.startswith('|') and line.count('|') >= 5 and not line.startswith('| 欄位') and not line.startswith('|--'):
                            total_fields += 1
                            parts = [p.strip() for p in line.split('|')]
                            if len(parts) >= 4 and parts[2] == '\u2014':
                                total_no_eng += 1
                                category = os.path.basename(root)
                                no_eng_list.append(f"{category}/{f}: {parts[1]}")

    print(f"  Total fields: {total_fields}")
    print(f"  With English Code: {total_fields - total_no_eng}")
    print(f"  Without English Code: {total_no_eng}")
    print(f"\n=== COMPLETE ===")


if __name__ == '__main__':
    main()
