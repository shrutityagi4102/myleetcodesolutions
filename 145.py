#Validate IP Address

"""Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi."""

class Solution:
    def checkstartzero(self,qp):
        l = [i for i in qp if len(i)!=1]
        m = [k for k in l if k[0]=="0"]
        return True if len(m)==0 else False
    
    def checkmid(self,qp,pat):
        ans = [i for i in qp if pat in qp]
        return True if len(ans)==0 else False
    
    def check(self,qp):
        qans = [i for i in qp if int(i)>=0 and int(i)<=255]
        return True if len(qans)==len(qp) else False
    
    def hexadeci(self,qp):
        checkhexa = [i for i in qp if i.isalnum() or i.isnumeric()]
        return True if len(checkhexa)==len(qp) else False
    
    def checklen(self,qp):
        qans = [i for i in qp if len(i)>=1 and len(i)<=4]
        return True if len(qans)==len(qp) else False
    
    def checkdigi(self,qp):
        checnum = [i for i in qp if i.isnumeric()]
        return True if len(checnum)==len(qp) else False
   
    def checkalpha(self,qp):
        q = []
        for i in qp:
            q = [k.lower() for k in i if k.isalpha()]
        alphas = ["a","b","c","d","e","f"]
        chq = [j for j in q if j in alphas]
        return True if len(chq)==len(q) else False

    def validIPAddress(self, queryIP: str) -> str:
        qp = queryIP.split(".")
        qx = queryIP.split(":")
        
        if len(qp)==4:
            if self.checkdigi(qp):
                if self.checkstartzero(qp) and self.checkmid(qp,"00") and self.check(qp):
                    return "IPv4"
                else:
                    return "Neither"
            else:
                return "Neither"
            
        elif len(qx)==8:
            if self.checkalpha(qp):
                if self.hexadeci(qx) and self.checklen(qx):
                    return "IPv6"
                else:
                    return "Neither"  
            else:
                return "Neither"
            
        return "Neither"
