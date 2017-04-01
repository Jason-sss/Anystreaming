import os
import re
import httplib2

OS = "Ubuntu"
GREEN_ON = "\033[1;32m ON \033[0m"
RED_OFF = "\033[1;31m OFF \033[0m"
STARTUP_LIST = ["Transcoder", "RtspGW", "RtmpGW", "Upload_92", "Upload_95", "ProxyTranscoder", "Livehttp", "SpeedMatrix"]
BASIC_SETTING_LIST = ["UDP_accept", "GRUB_time"]

root_path = "/opt/anystreaming/"
path_92 = root_path + "upload/92/cfg.lst"
path_95 = root_path +  "upload/95/cfg.lst"
path_proxyTranscoder = root_path + "proxyTranscoder/cfg.lst"
path_source = root_path + "vas/source/cfg.lst"
path_static = root_path + "vas/static/cfg.lst"
path_dynamic = root_path + "vas/dynamic/cfg.lst"
path_livehttp = root_path + "livehttp/cfg.lst"


''' 
	get filted info from cfg.lsts
'''

def get_vas_cfg_lst():
	print("upload_92:")
	with open(path_92) as pf:
		for line in pf.readlines():
			if "accessport=" in line or "reptservice=" in line or "rept4online=" in line or re.findall(r'^l=', line):
				print("\t", line, end="")
	print()

	print("upload_95:")
	with open(path_95) as pf:
		for line in pf.readlines():
			if "accessport=" in line or "reptservice=" in line or "rept4online=" in line or re.findall(r'^l=', line):
				print("\t", line, end="")
	print()

	print("proxyTranscoder:")
	with open(path_proxyTranscoder) as pf:
		for line in pf.readlines():
			if "accessport=" in line or "rept4online=" in line or re.findall(r'[a-z]{4}_[a-z]{4}=', line) or re.findall(r'^l=', line):
				print("\t", line, end="")
	print()

	print("source:")
	with open(path_source) as pf:
		for line in pf.readlines():
			if "using_UTC" in line or "SCH=" in line or "reptservice=" in line or re.findall(r'^l=', line):
				print("\t", line, end="")
	print()

	print("static:")
	with open(path_static) as pf:
		for line in pf.readlines():
			if "using_UTC" in line or "SCH=" in line or "reptservice=" in line or re.findall(r'^l=', line):
				print("\t", line, end="")
	print()

	print("dynamic:")
	with open(path_dynamic) as pf:
		for line in pf.readlines():
			if "using_UTC" in line or "SCH=" in line or "reptservice=" in line or re.findall(r'^l=', line):
				print("\t", line, end="")
	print()

	print("livehttp:")
	with open(path_livehttp) as pf:
		for line in pf.readlines():
			if "accessport=" in line or "rc=" in line or re.findall(r'^l=', line):
				print("\t", line, end="")
	print()


'''
 根据查看元素是否存在于list中，来显示ON或OFF
'''
def status_print(modules, type=0):
	if type == 0:	# 开机启动项
		for module in STARTUP_LIST:
			if module in modules:
				if module == "RtspGW" or module == "RtmpGW":
					print("\t" + module + "\t\t\t", GREEN_ON)	
				else:
					print("\t" + module + "\t\t", GREEN_ON)
			else:
				if module == "RtspGW" or module == "RtmpGW":
					print("\t" + module + "\t\t\t", RED_OFF)
				else:
					print("\t" + module + "\t\t", RED_OFF)
	elif type == 1:	# 基本设置
		for module in BASIC_SETTING_LIST:
			if module in modules:
				print("\t" + module + "\t\t", "\033[1;32m SET \033[0m")
			else:
				print("\t" + module + "\t\t", "\033[1;31m NOT SET \033[0m")

'''
 检查服务器的基本配置项
'''
def check_server():
	os.system("date")
	# 检查系统及内核版本
	print("\033[1;40mCheck os...\033[0m")
	with open("/etc/issue") as of:
		data = of.readline()
		OS = data.split()[0]
		print("\t" + data, end="\t")
	with open("/proc/version") as vf:
		data = vf.readline()
		print("kernel:", data.split()[2])


# 检查开机启动脚本
	print("\033[1;40mCheck startup service...\033[0m")
	services = []
	if OS == "Ubuntu":
		with open("/etc/rc.local") as lf:
			for line in lf.readlines():
				if re.findall(r'^#', line):
					pass
				else:
					if "/opt/anystreaming/transcoder/rund" in line:
						services.append("Transcoder")
					elif "/opt/anystreaming/rtspgw/rund" in line:
						services.append("RtspGW")
					elif "/opt/anystreaming/rtmpgw/rund" in line:
						services.append("RtmpGW")
					elif "/opt/anystreaming/upload/92/rund" in line:
						services.append("Upload_92")
					elif "/opt/anystreaming/upload/95/rund" in line:
						services.append("Upload_95")
					elif "/opt/anystreaming/proxyTranscoder/rund" in line:
						services.append("ProxyTranscoder")
					elif "/opt/anystreaming/livehttp/rund" in line:
						services.append("Livehttp")
					elif "/opt/anystreaming/speedmatrix/rund" in line:
						services.append("SpeedMatrix")
		status_print(services)
	else:
		print("Not Ubuntu Server!")
	

# 检查基本配置项
	print("\033[1;40mCheck basic settings...\033[0m")
	settings = []
	if OS == "Ubuntu":
	# 接收udp组播
		with open("/etc/sysctl.conf") as ef:
			count = 0
			for line in ef.readlines():
				if "net.ipv4.conf.default.rp_filter=0" in line:
					count += 1
				if "net.ipv4.conf.all.rp_filter=0" in line:
					count += 1
			if count == 2:
				settings.append(BASIC_SETTING_LIST[0])

	# 优化开机等待时间
		with open("/boot/grub/grub.cfg") as gf:
			count = 0
			for line in gf.readlines():
				if "set timeout=2" in line:
					count += 1
			if count == 2:
				settings.append(BASIC_SETTING_LIST[1])

		status_print(settings, type=1)

	# 检查本机IP
	



	else:
		print("Not Ubuntu Server!")




if __name__ == "__main__":
	check_server()
