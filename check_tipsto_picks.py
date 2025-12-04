# import requests
# from bs4 import BeautifulSoup
# import smtplib
# from email.mime.text import MIMEText
# import time
# import os

# # ------------------------------------------
# # CONFIG
# # ------------------------------------------
# URL = "https://www.betrush.com"
# TIPSTER_NAME = "Tipsto"
# SEEN_FILE = "seen_tipsto.txt"    # stores already-seen picks

# # EMAIL SETTINGS
# SMTP_SERVER = "smtp.gmail.com"   # If using Gmail
# SMTP_PORT = 587
# EMAIL_USER = "testingformerightnow@gmail.com"      # <-- your email
# EMAIL_PASS = 'jzvq wyhk xrkp qynt'         # <-- Gmail app password (not normal login)
# EMAIL_TO = "ahmadmubashir9009@gmail.com"         # where to send notification nikolab96@yahoo.com"
# # ------------------------------------------


# def send_email(subject, body):
#     msg = MIMEText(body)
#     msg["Subject"] = subject
#     msg["From"] = EMAIL_USER
#     msg["To"] = EMAIL_TO

#     server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
#     server.starttls()
#     server.login(EMAIL_USER, EMAIL_PASS)
#     server.sendmail(EMAIL_USER, EMAIL_TO, msg.as_string())
#     server.quit()


# def load_seen():
#     if not os.path.exists(SEEN_FILE):
#         return set()
#     with open(SEEN_FILE, "r", encoding="utf-8") as f:
#         return set(line.strip() for line in f.readlines())


# def save_seen(seen_set):
#     with open(SEEN_FILE, "w", encoding="utf-8") as f:
#         for item in seen_set:
#             f.write(item + "\n")


# def fetch_tipsto_picks():
#     response = requests.get(URL)
#     soup = BeautifulSoup(response.text, "html.parser")

#     picks = []
#     rows = soup.select("table.picks tr")  # rows from the picks table

#     for row in rows:
#         cols = row.find_all("td")
#         if len(cols) < 7:
#             continue

#         tipster = cols[-1].get_text(strip=True)
#         if TIPSTER_NAME in tipster:
#             match_title = cols[1].get_text(strip=True)
#             pick_str = TIPSTER_NAME + " - " + match_title
#             picks.append(pick_str)

#     return picks


# def main():
#     print("Checking Tipsto picks...")

#     seen = load_seen()
#     current_picks = fetch_tipsto_picks()

#     new_picks = [p for p in current_picks if p not in seen]

#     if new_picks:
#         print("NEW TIPSTO PICK FOUND!")
        
#         message = "New Tipsto picks:\n\n" + "\n".join(new_picks)
#         send_email("New Tipsto Pick Alert", message)

#         seen.update(new_picks)
#         save_seen(seen)
#     else:
#         print("No new Tipsto picks.")

#     print("Done.")


# if __name__ == "__main__":
#     main()






import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import time
import os

# ------------------------------------------
# CONFIG
# ------------------------------------------
URL = "https://www.betrush.com"
TIPSTER_NAME = "Tipsto"
SEEN_FILE = "seen_tipsto.txt"    # stores already-seen picks

# EMAIL SETTINGS
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = "testingformerightnow@gmail.com"
EMAIL_PASS = "jzvq wyhk xrkp qynt"
EMAIL_TO = "nikolab96@yahoo.com"
# ------------------------------------------


def send_email(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_TO

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASS)
    server.sendmail(EMAIL_USER, EMAIL_TO, msg.as_string())
    server.quit()


def load_seen():
    if not os.path.exists(SEEN_FILE):
        return set()
    with open(SEEN_FILE, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f.readlines())


def save_seen(seen_set):
    with open(SEEN_FILE, "w", encoding="utf-8") as f:
        for item in seen_set:
            f.write(item + "\n")


# def fetch_tipsto_picks():
#     response = requests.get(URL)
#     soup = BeautifulSoup(response.text, "html.parser")

#     picks = []

#     # Each pick row inside table.picks
#     rows = soup.select("table.picks tr")

#     for row in rows:

#         # TIPSTER NAME column → <td class="right_td">
#         tipster_td = row.find("td", class_="right_td")
#         if not tipster_td:
#             continue

#         tipster_text = tipster_td.get_text(strip=True)

#         # Check: is this row from Tipsto?
#         if TIPSTER_NAME not in tipster_text:
#             continue

#         # MATCH TITLE column → <td class="pick_descr">
#         match_td = row.find("td", class_="pick_descr")
#         if match_td:
#             match_title = match_td.get_text(strip=True)
#         else:
#             match_title = "Unknown Match"

#         pick_str = f"{TIPSTER_NAME} - {match_title}"
#         picks.append(pick_str)

#     return picks
# def fetch_tipsto_picks():
#     response = requests.get(URL)
#     soup = BeautifulSoup(response.text, "html.parser")

#     picks = []

#     rows = soup.select("table.picks tr")
#     for row in rows:
#         # TIPSTER NAME
#         tipster_td = row.find("td", class_="right_td")
#         if not tipster_td:
#             continue
#         tipster_text = tipster_td.get_text(strip=True)
#         if TIPSTER_NAME not in tipster_text:
#             continue

#         # MATCH TITLE inside <td class="picktooltip"> -> <a>
#         match_td = row.find("td", class_="picktooltip")
#         if match_td:
#             a_tag = match_td.find("a")
#             match_title = a_tag.get_text(strip=True) if a_tag else "Unknown Match"
#         else:
#             match_title = "Unknown Match"

#         pick_str = f"{TIPSTER_NAME} - {match_title}"
#         picks.append(pick_str)

#     return picks



# def fetch_tipsto_picks():
#     response = requests.get(URL)
#     soup = BeautifulSoup(response.text, "html.parser")

#     picks = []

#     rows = soup.select("table.picks tr")
#     for row in rows:
#         # TIPSTER NAME
#         tipster_td = row.find("td", class_="right_td")
#         if not tipster_td:
#             continue
#         tipster_text = tipster_td.get_text(strip=True)
#         if TIPSTER_NAME not in tipster_text:
#             continue

#         # TIPSTER link inside <a> in right_td
#         a_tag_tipster = tipster_td.find("a")
#         if a_tag_tipster and a_tag_tipster.has_attr("href"):
#             tipster_link = a_tag_tipster['href']
#             # prepend base URL if relative
#             if not tipster_link.startswith("http"):
#                 tipster_link = URL.rstrip("/") + "/" + tipster_link.lstrip("/")
#         else:
#             tipster_link = "No URL"

#         # MATCH TITLE inside <td class="picktooltip"> -> <a>
#         match_td = row.find("td", class_="picktooltip")
#         if match_td:
#             a_tag_match = match_td.find("a")
#             match_title = a_tag_match.get_text(strip=True) if a_tag_match else "Unknown Match"
#         else:
#             match_title = "Unknown Match"

#         # Combine into final string
#         pick_str = f"{TIPSTER_NAME} - {match_title} ({tipster_link})"
#         picks.append(pick_str)

#     return picks





from seleniumbase import SB
from bs4 import BeautifulSoup
import time

def fetch_tipsto_picks():
    with SB() as sb:
        sb.open("https://www.betrush.com")
        sb.sleep(3)  # allow JS to load picks table

        html = sb.get_page_source()

    soup = BeautifulSoup(html, "html.parser")
    picks = []

    rows = soup.select("table.picks tr")
    for row in rows:

        # 1️⃣ Tipster Name (inside td.right_td > a)
        tipster_td = row.find("td", class_="right_td")
        if not tipster_td:
            continue

        a_tag_tipster = tipster_td.find("a")
        if not a_tag_tipster:
            continue

        tipster_text = a_tag_tipster.get_text(strip=True)
        if TIPSTER_NAME.lower() not in tipster_text.lower():
            continue

        # Tipster URL
        tipster_link = a_tag_tipster.get("href", "")
        if tipster_link and not tipster_link.startswith("http"):
            tipster_link = URL.rstrip("/") + "/" + tipster_link.lstrip("/")

        # 2️⃣ Match Title
        match_td = row.find("td", class_="picktooltip")
        if match_td:
            match_a = match_td.find("a")
            match_title = match_a.get_text(strip=True) if match_a else "Unknown Match"
        else:
            match_title = "Unknown Match"

        pick_str = f"{TIPSTER_NAME} - {match_title} ({tipster_link})"
        picks.append(pick_str)

    return picks




def main():
    print("Checking Tipsto picks...")

    seen = load_seen()
    current_picks = fetch_tipsto_picks()

    new_picks = [p for p in current_picks if p not in seen]

    if new_picks:
        print("NEW TIPSTO PICK FOUND!")

        message = "New Tipsto picks:\n\n" + "\n".join(new_picks)
        send_email("New Tipsto Pick Alert", message)

        seen.update(new_picks)
        save_seen(seen)
    else:
        print("No new Tipsto picks.")

    print("Done.")


if __name__ == "__main__":
    main()




