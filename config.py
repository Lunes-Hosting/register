#Constants Variables

#github
GITHUB_REPO = "BlossomDNS/register"
GITHUB_SUBDOMAIN_JSON = f"https://raw.githubusercontent.com/{GITHUB_REPO}/main/subdomain.json"
#cloudflare
CLOUDFLARE_API_TOKEN = ""
CLOUDFLARE_ACCOUNT_ID = ""

#DNS Records publishing
PROXIED_ON = False
TTL_INT = 1
#domain you are giving subdomains away
CLOUDFLARE_DOMAINS = []
#admin
import admins
ADMIN_ACCTS = [
                admins.Admin(id=1, username="test@test", password="test"), 
                admins.Admin(id=2, username="test", password="test")
               ]
#git auth
CLIENT_SECRET = ""
CLIENT_ID = ""