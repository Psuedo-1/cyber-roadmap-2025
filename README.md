⸻

Joshua — 12‑Month Cybersecurity & Cloud Roadmap (First‑Year Project)

A complete, actionable plan you can put in a project folder. Everything is organised so you can copy/paste, follow, and check off tasks.

⸻

Project Overview
	1.	Immediate setup (what to do right now, commands included)
	2.	Weekly schedule for the next 12 months
	3.	12 staged projects (monthly)
	4.	Free courses and platforms (AWS, Cloudflare, TryHackMe, etc.)
	5.	Tools, VS Code extensions, install commands
	6.	Internship hunt plan, sample message, CV checklist
	7.	How to present work: GitHub/README/blog templates
	8.	Interview prep checklist
	9.	Notes for remote hiring from the Cayman Islands
	10.	Progress tracker & milestone checklist

⸻

1) Immediate Setup — Do This Right Now

Install Homebrew (macOS)

/bin/bash -c “$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)”

Install Python, pip, virtualenv

brew install python
pip3 install –user virtualenv

Install security tools & Docker

brew install nmap
brew install john
brew install sqlmap
brew install –cask wireshark
brew install –cask docker

Install AWS CLI

brew install awscli
aws –version

Create project folder

mkdir -p ~/cyber_projects && cd ~/cyber_projects
code .

⸻

2) Weekly Schedule (First 12 Weeks, Then Monthly)

Daily (30–90 mins)
	•	One small task: TryHackMe room, Python script, or reading

Weekly (4–8 hrs)
	•	2 × TryHackMe/HackTheBox rooms
	•	1 × AWS cloud lab
	•	1 × project or writeup

Weeks 1–12
	•	Week 1: Install tools, create GitHub, TryHackMe “Complete Beginner”
	•	Week 2: Docker + Kali container, basic Linux + local nmap scan
	•	Week 3: AWS free tier EC2 deployment
	•	Week 4: Python auth log monitor
	•	Weeks 5–8: TryHackMe Pre‑Security + Intro to Defensive Security
	•	Weeks 9–12: Deploy DVWA on EC2 + test vulnerabilities

Months 4–12
	•	Months 4–6: Cloud security labs, AWS IAM
	•	Months 7–9: SOC/alerting project + blue team
	•	Months 10–12: Internship applications, mock interviews

⸻

3) 12 Staged Projects (One Per Month)

1. Environment & Tools

Document installs, commands, screenshots.

2. Python Log Monitor

Script that watches auth logs and prints alerts.

3. Local Network Mapper

nmap subnet scan → CSV + hardening notes.

4. Kali in Docker + Recon Scripts

Containerised Kali with Bash/Python recon tools.

5. Secure Web App on AWS

Small web app, HTTPS, security groups, documentation.

6. DVWA Pentest

Attack your deployed DVWA + write findings/fixes.

7. ELK Logging & Alerting PoC

Ship logs to ELK or create lightweight log alerts.

8. AWS IAM Hardening Playbook

Least privilege roles + MFA simulation.

9. SOC Incident Response Playbook

Simulate incident + forensics workflow.

10. Threat Intel Report

Pick recent CVE/malware → 2–3‑page report.

11. Automation Intro

Terraform or Ansible project.

12. Capstone

Secure cloud app + logging + CI checks.

⸻

4) Free Courses & Ordered Learning Path

Immediate (0–3 months)
	•	TryHackMe: Complete Beginner path
	•	AWS: Security Fundamentals (free)
	•	Cloudflare: Getting Started w/ Cloudflare Security

Next (3–6 months)
	•	TryHackMe: SOC Analyst Path
	•	AWS Solutions Architect Basics
	•	OverTheWire: Bandit

Intermediate (6–12 months)
	•	TryHackMe Offensive Rooms
	•	AWS: GuardDuty, KMS, CloudTrail deep dives
	•	Intro to Networking (any MOOC)

⸻

5) Tools & VS Code Extensions

VS Code Extensions
	•	Python
	•	Docker
	•	Remote SSH
	•	Terraform
	•	YAML
	•	REST Client
	•	GitLens

Tools (installed earlier)
	•	Python
	•	Docker
	•	nmap
	•	john
	•	sqlmap
	•	Wireshark
	•	AWS CLI

⸻

6) Internship Hunt — Where to Look

Where to search
	•	LinkedIn (remote, cybersecurity intern)
	•	Indeed
	•	Glassdoor
	•	CrowdStrike, Palo Alto, Cloudflare, AWS careers
	•	TryHackMe community boards
	•	University of Leicester CS staff

Sample Outreach Message

Hi,

I’m Joshua, a first‑year CS student at the University of Leicester building hands‑on cybersecurity experience (TryHackMe progress, AWS labs, GitHub projects). I’m looking for a remote part‑time Security Intern or SOC Analyst opportunity. I can commit 10–12 hours/week and already have a working macOS lab with Docker and AWS. Could we schedule 15 minutes to discuss potential roles?

Thanks,
Joshua

CV Checklist
	•	1‑line summary: degree, year, cybersecurity goal
	•	Skills: Linux, Python, AWS, Docker, nmap, Wireshark
	•	Projects: 3 lines each + GitHub links
	•	Education: University of Leicester
	•	Contact: email, LinkedIn, GitHub

⸻

7) How to Present Work (GitHub)

Repo Structure

project-name/
README.md
scripts/
docs/
infra/

README Template
	•	Title
	•	One-line summary
	•	Tools used
	•	Steps to reproduce
	•	Learning outcomes
	•	Screenshots

⸻

8) Interview Prep Checklist
	•	Networking: TCP/IP, HTTP, DNS, SMTP
	•	Linux: permissions, processes, SSH, logs
	•	Python: regex, parsing logs
	•	Cloud: IAM, VPC, SGs, CloudTrail, KMS
	•	Tools: nmap, Wireshark, sqlmap, Burp basics
	•	Soft skills: explaining projects

⸻

9) Remote Hiring Notes (Cayman Islands)
	•	As a British citizen, most UK remote roles accept you
	•	Some prefer contractor agreements — check terms
	•	Mention UTC‑5 availability
	•	On CV: “Open to remote work (Cayman Islands, UTC‑5)”

⸻

10) Progress Tracker (MILESTONES.md)
	•	Environment set up
	•	GitHub repo created
	•	TryHackMe Complete Beginner
	•	AWS EC2 web server deployed
	•	Python log monitor completed
	•	3 TryHackMe rooms documented
	•	DVWA pentest lab done
	•	Applied to 10+ internships
	•	Completed mock interview
	•	Secured an internship or freelance gig

⸻

Final Notes
	•	Copy this document into your repo
	•	Update milestones weekly
	•	Keep screenshots in docs/
	•	Push early and often

⸻