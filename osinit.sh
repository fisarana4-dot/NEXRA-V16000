#!/data/data/com.termux/files/usr/bin/sh
P=0;F=0
c(){ if eval "$2" >/dev/null 2>&1; then
echo "OK: $1";P=$((P+1));else
echo "FAIL: $1";F=$((F+1));fi;}
c "dig" "command -v dig"
c "nslookup" "command -v nslookup"
c "whois" "command -v whois"
c "setcap" "command -v setcap"
c "dns" "dig +short example.com | grep -q 104"
echo "PASS=$P FAIL=$F"
[ $F -eq 0 ] && echo HEALTHY || echo ISSUES
