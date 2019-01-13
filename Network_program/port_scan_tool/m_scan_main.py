from m_domain_name import *
from m_ip_address import *
from m_make_folder import *
from m_nmap import *
from m_robots_scan import *
from m_whois import *

#sites 폴더 밑 각 사이트 정보를 쌓자
ROOT_DIR = 'sites'
create_dir(ROOT_DIR)

def gather_info(name, url):
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(url)
    nmap = get_nmap(' -F', ip_address)#F옵션은 빠르게 스캔하라는뜻
    robots_txt = get_robots_txt(url)
    whois = get_whois(domain_name)
    create_report(name, url, domain_name, nmap, robots_txt, whois)
    pass
def create_report(name, full_url, domain_name, nmap, robots_txt, whois):
    project_dir(ROOT_DIR + "/" + name)
    create_dir(project_dir)
    write_file(project_dir + "/full_url.txt", full_url)
    write_file(project_dir + "/domain_name.txt", domain_name)
    write_file(project_dir + "/nmap.txt", nmap)
    write_file(project_dir + "/robots_txt.txt", robots_txt)
    write_file(project_dir + "/whois.txt", whois)
gather_info("tistory", "https://www.tistory.com/")