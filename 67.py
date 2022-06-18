#Defanging an IP Address

"""Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".""""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        for i in address:
            if i==".":
                ans += "[.]"
            else:
                ans +=i
        return ans
