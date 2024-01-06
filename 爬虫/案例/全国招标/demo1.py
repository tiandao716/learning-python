# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-04 19:42
"""
import base64

from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad


def decrypt(msg):
    """
    DES解密
    :param msg: 需要解密的字符串
    :return: 解密后的字符串
    """
    #  密钥，必须是8位
    # key = "1qaz@wsx".encode('utf-8')
    # # print(type(key))
    # #  初始化DES对象
    # des = DES.new(key=key, mode=DES.MODE_ECB)
    #  加密
    # encrypted_text = des.encrypt(msg.encode('utf-8'))
    # # 转base64
    # encrypted_text_base64 = base64.b64encode(encrypted_text).decode('utf-8')

    #
    key = "1qaz@wsx".encode('utf-8')
    # print(type(key))
    des = DES.new(key=key, mode=DES.MODE_ECB)
    # s = "JwdsCjMM05e4niaZd3zOKXjfJCSKzfLUd1joO6+H0TGjmj0y4AzXIiFlVNgGu02jceOtRHg1DQaWtciXm1k9z9ZODgf7rWX3QS5erHds5AEmBpYRRmpc1P5G/ea+css5EDpX5nE5rlcQjT1HcceFJxfz18IdukhELTOyKstyPkRWQMpq+9brgxjewzt4ZCij8MtXdF6v8B5egdS5xT5J70znI/JDBV1AyR9zFHUQDdH6npMrdCLFT9R+degOEAL8HYsAsYAsCHP4vUiPOzsaUqoRxFR2Fjg3zGK7BQFiyK/fZtwrkSQSpDlprNfenfdk7e74S0gXMVKVEd+nIYTve+sDTSynnb+awU+EpYjOK6DCbnt9PUSrRg4SAXdlpz5pcqmAoPgeT6maAEFmxsSzkKql6nKA+HXsn05Ep20ttjc56q0+M/IPspwR1nn87TK3iAGr905Q3ZR/V+zqF7lYRAJeDnMo/aGLfNVcEtaCb5Wm7Rjtjynqky0omrG4WqKguGwPm1GZMOu5DUAEm/FeZaHTCvTDNc7BIFh1pqMsWEZI0r1Ikt7Cm0861XZpnMKzynIQ3cuK9EGz9rrQuQuTehScksfWL8PvSCFXJp5krAg6icCZeOheG+sXGLIsY36rhW49uKJG5k+2IfdrgnWBqUjI4M4Me9cb6hxP4inaldeDuGiBaL7hFpu03u1fBKOBgvNxEZ4NXbrfaE2egdgpLOO82XNl7Xth+MmVQtjj6ioXBTO9FtBoP7cKFpwJZwptugTuWHLWw/dPOtV2aZzCs3ynR1pp4ueQFAQkeqH9fYbCliredcZpOLn877pG4TDAIJWOkyxubo4ryVjfLEZfj+sXGLIsY36rhW49uKJG5k+2IfdrgnWBqUjI4M4Me9cbqL5ojMkh88zEwQFdbKdy7UdLKGiT0VZwdCVPshv1+yRlVt+ebsbl4nyhPdSJOZV1pd4I8PlMflLmRwtfCEiAc4rk6R13tiHIfQhFyL4//HO20L836/FeMWbdpBJ7SeFl0mGWZbr8rZVPpgwM4GLZkHZhlpWKph0YZf4nW13QMZAtgDwvsaBRB1VhkwAhzTBMLJ1gVWvOPW9G0XE880rMYLGAXAxzrzLlN+LgsC28Rrw41mG5Zh/cegrY0wh1pF0UjCidE0vLCzq/vqXzqkl31uB6hLXVhvX+j+/qONAeXUOGOJYu7VKCnFQ4ExAgBVRdw3JsaCN2pjFkDWXwxvzJYhrMzAiOOUg5CUAy3l/ypVFsbVGAYVMO/NmQyTxGuTwdT61kVd+hHEQMo37mz87vzafSmbry7mLcbuTSc09tBnLvjOuvV2UaTW14aDfoGPNAipN3+CSy4pvONLa3dn3wABvKZXs5kE69hJQzBgcWPTFtVcR7mK4R1u89QsZyXKU0em5Q90eajB9ZTsNxHWu0ao725jcoObxldTXdiWB8//AZy11ugmFpehfBbl5vTkH494ijn7ORmRCaAEFmxsSzkKoIMPaVku3E9zBYKEJUBeTx+ygLmVp2vDSbKYMjZ/zrK7vzsq/sa4frQI0Ah2SVVnLCUQjgXJ6zPhOLU0Rpxzcdca6fFsCuMHBPN0Jbsd12ex6ivGctZR1ITsRHDBzme/vLAeMdL3uR1Dz9e1Nn3TxDuuOs+fHqRUUEDszAnjARzGVu7/DgIUuxwrW9/wdEI93+2ulekDOU51SWHdgckYiKH2hNcp08H26HMgDbag4pqYpTF4UBKvcck0JXApKzfa7gaImvJmYocrhbP8rIAK4tTGkbSleWCmQNZfDG/MliK76euM523nc8c63Q7dnivUbs/EOiR5Id22onlFF7hAZLijgfTO6hkOtzOv0XMvIUl9xyoXzqi3ANvfnMZ4Mlmqj4AW0JzhzcXoHUucU+Se9uhzIA22oOKamKUxeFASr3HJNCVwKSs32u4GiJryZmKHK4Wz/KyACuLUxpG0pXlgpkDWXwxvzJYiu+nrjOdt53PHOt0O3Z4r1G7PxDokeSHdtqJ5RRe4QGS4o4H0zuoZDrczr9FzLyFJfccqF86otwDb35zGeDJZqo+AFtCc4c3F6B1LnFPknvFrbidQ27nhhrFMMhDCgPwOn0IIqU/4lLjY9j1JaLZbHMYrsFAWLIr229T4CvvZHYn7+eo0LnxrxVt6Aa5vEEv963cyZ/XCmXo93mwDi1YnqGH9ed+wA56fQb5yXT2+S1HLcaIbbAQiOaAEFmxsSzkP+rbkhCzBRBwTIB+tQW7IZM5yPyQwVdQDwZRtPPGquWYAyyjHtyw41eIhqaZ9XYt5ePqvkXxdre6OuvTNjmqejx4pV3stGQ2Un7X5Xut6KW0mGWZbr8rZXDlC/zhtST3MkXwg6CEr3iupkApRuwS7tQ7U5GMV3Utylb++6SA0rDng+dPtkL6hIa0gIehWyublQzAwPTPtZVXPor6IgQqAhlEZuX2YT2Icp30x+LUQVKab5rpy50iFZnDWnkfCSUBbLtCNLxR+2RRWKY14lqETRRE48aEZwcrb4T6U2RCSTMiO/tfn3jyQaTr6K52DoCUyrNzLjPGAGju1daWwqc/1uDM2IDqSVZomW9oT0zjtfaRIV6pStr3gNKY0wgsjEkPVz6K+iIEKgIZRGbl9mE9iHKd9Mfi1EFSmm+a6cudIhWZw1p5HwklAVegdS5xT5J760TldBaCiTQYxUfJqmGWZS32p618wsEbOjVS6Rl984qMZDizb2cyavc8cRqhkMMD3E/v27rReuzpboYIy8p+vV2zk62VE4j6Ip9NfvUagPuJLkLmNl2T5gQ5N3oHUUSbU8hIyixZKVZc+DfGjX39xmdhtbHSXa4O4izQaD5M0g2W9GtQz7BlM2PGpQnwSGL53rqhZ7TnHe+GQyVTqwsJMe7QD2mdOWF/jUA8ZunR00CYAO7ng/GQDQWVJmzwI0guyZ7HSI/7MJDUOibXe2xzVZU1DSAhdUV+gaZmOH7HNoHCbCSK9lxaaXKJGIf0AjV0UmtaDVWU8qD/pTwVnGu4Tk8MQbo4GTFiUoLlyb4Azu1VeV80AGK4RXifGnp89k5FhUJOeuHv4K0JiBRc25zyiZ6AcEEsLoqL5B90v/eXJYEA/CqJXQ9U7lKLl0BrXkrzCTruNmKzk608l/MfEVl3O2JKubSjUH/BUEn8TyGhlvxjUuQMMqmzrjvXOxWLk758EdaYx9m8C2c/roKWbVNcwR+mHop9eDnXc6n59MrCGakQ7cHmGiyZ1U7Glc2LRKQCsRIyrf+tzBFEcmG+vWshyKoXu4lIFXEUPlj+YFskS+vco63zHw1k92eWTp7rSy4vfx6O1kXon4DmgBBZsbEs5Dq2jszhQG2HFyYR7mNos88Ht4ycXFsriyYJ181qGe68JMllSDhggeMRY7Zpzp+DhNnZDm1yS4b+DuC/Hw56iug5WfQ5k5ahfaeKhwlL4zA4poAQWbGxLOQIdtfCl0NjU6tOWrXcJr4g1jVg24zxPKzcBVw9chWQFuxCYVmqVwK+zQC+UXpdxRFpHr2os8hvoxWi63D754DRvzjAIe3NVgR+KwNZ8R4iCAZoKi7nDiaG3BPN0Jbsd122QoQ6thgBE4cQuqsz9Sjicg22GJUK65jRY7Zpzp+DhO9BZUU+1UfQWA/9tTwJs6lupk/Y1/mP+70HPVprlYYRJSElX4Fql/6ThHoN8DR4oR0cvhTQS43BXbkjVX8CG3ZlV9PWyD2kLDMB/f330XQu1r51xjPp+e7kvIRia3e4SDc8bnMmKoe9NbFtEA9Z1w7a7IV6auYxVzuKFoJ9Fm14X+bEvXn9yHzZSQrCQsg9eUejCb1QiuWmOsjsdfJrnVrIF3dMQySXFcN5A98nDWGFwSz1uDb85JfHRSl29GhqC/LxYVIZ+Crb3bKYyuEHK/YmTGMvydQWvyhL+wCtLau+LGBZoDN2qBksVquYYarNyb7k3NKOB2/Dous440BzGEIWyOGwx4blzVLLJMli57YXH7jcmbYTOPGn+qDH91Ll50271ZKrxA3PX6zIf7lWPADlVvdCN0S4fj3kady7Byk0KP1HulnNyNv6kFGdcHVYxn+cEXlsW/mTiFkrcVVdPDBVDxY40pHcRvO7A9ZWmBAw1JoMzK8t1EThbUibUImfoWP2cCS90e3CHIDrwQ8g1e1XoHUucU+Se8WtuJ1DbueGJZN82lu7t+S/sSwtU81Kc1KTyZONo7G3t1xKSfnymZuXASrsuQcInXqSTDWaHsZAp/RTJ3kvAPJ+6ksrxNpR9YIB3K6qsFZm8F0lujChFL9qPQP6HbnuNBSFG6WbaA3TByLCJPk6iPUzcNLO/V9YAKNg795xiNW7Termo1qcXqFOeqtPjPyD7LM/DQpqvDUTE1JfwhrHgG1/5cx/A5BkoV15x3nfIsama0sJpICuyBtAw9RAyLV8eXJFb1X9he+w5O/PykuqhMQVZzAgNqG+APGtEOfhFUk1wRby1vDS8jT+1CBV3iSVXeT+XxEpvpfYpYj5fhcnfZLQSw6HL9iL9TMyK8je0PqeQcpkQwCPwE7nUlkt2CY0do0RX5zmfB17i2APC+xoFEH14JL1/NumT+g3Xv41hx/ZN8wu7gUDnS4OrAauWk664dIyODODHvXG+ocT+Ip2pXX6/ZULkhJThRzz2HrQZ8OGy0C2/mNoHsUjvXHgXL4wuRm6psP6lRhgYSUMwYHFj0xpjxhVF7y2edLqV+bknrVFWCxiR5sBqUaLM0SYpBN6HiLsohCyO82Y7tXWlsKnP9bgzNiA6klWaJlvaE9M47X2kSFeqUra94DSmNMILIxJD3MyK8je0PqecgFvq1X2ZnRxxKt3ZjzkebLYImGQQ+QqreQDETSpcUQ/TtiuxeIbaPYEfLs5rCkLgpmVd7sc1C0PxsQcb7RbBt84Ap94mjffUN4dqNQRP8dS0SEmoGe1XrcHJ5kJB88fNDgYfFZw1xkW27unPjAOk+6sw2rPSrhaTOZxyMBUk4KGk73wnmeuNqWTfNpbu7fkhZh9yd3A4Ky6qr5o+ppX9UBGC7KSmRVmcmDe/mIED0xiuTpHXe2Ich9CEXIvj/8c7bQvzfr8V4xZtn0BpIDuJypYnV7gOn+noXtGItBiEJIdmGWlYqmHRhl/idbXdAxkC2APC+xoFEHVWGTACHNMEwsnWBVa849b0bRcTzzSsxgsYBcDHOvMuU34uCwLbxGvDjWYblmH9x6CtjTCHWkXRSMKJ0TS8sLOr++pfOqSXfW4HqEtdWG9f6P7+o40B5dQwbLSal87+d+bDBpLtNq7iVAyX9JoNLj92c2wVlI9Z1OZA1l8Mb8yWIazMwIjjlIOQlAMt5f8qVRbG1RgGFTDvzZkMk8Rrk8HU+tZFXfoRxEDKN+5s/O782n0pm68u5i3G7k0nNPbQZy74zrr1dlGk1teGg36BjzQIqTd/gksuKbzjS2t3Z98AAbymV7OZBOvYSUMwYHFj0xbVXEe5iuEdbvPULGclylNHpuUPdHmowfWU7DcR1rtGqO9uY3KDm8ZXU13YlgfP/wGctdboJhaXoXwW5eb05B+PeIo5+zkZkQmgBBZsbEs5CqCDD2lZLtxPcwWChCVAXk8fsoC5ladrw0mymDI2f86yu787Kv7GuH60CNAIdklVZywlEI4Fyes7AJS8/VY/4OFDYE3vaJxD5FjtmnOn4OE/22nK2iOmYQGnRyuO442sJ2ZivZemNwDSFlVNgGu02jWVIGpMBwS2S7KKn26HJhikatzVXllLjhCYLIgrUWdIDMDRyJGhSlX/5G/ea+css5EDpX5nE5rldnHK9/jfQii4go/JseHXwZCAeqMnl8QsKKu7hM7+TkY2N57LrHYNXmORg7PUaX9niaz96ci6SibAOd2YLWWTRTpTt3toiHYavTXuo7QgBtX8mv2tUbFTx8Exg331+zNKprcYARCQN1bkYqfYlcd6J2hWID04eVIkfOo3oACDyZX53kZ6jXdlaHdaQHOYGlIaj1+OpV0c9jE4INrAV4W2O51nKAJ+rQzXFOEOT6ptjCvn/oQ2awLiKje5Lxn/3Lyi3AVOuqaAXg57kvYpxtcFqV0EZE/o1YDUbyajBIRJduKA3ZK2pN7klF4xbvTth98Treg38yfH4kEF6B1LnFPknvFrbidQ27nhhC7FQe/CG+Q/7EsLVPNSnN7zyW2Et794fr/pyVHPqo6+GG2xVTW9xgUhRulm2gN0wciwiT5Ooj1M3DSzv1fWACjYO/ecYjVu03q5qNanF6hTnqrT4z8g+yzPw0Karw1ExNSX8Iax4Btf+XMfwOQZKFdecd53yLGpmtLCaSArsgbQMPUQMi1fHl9av/HuHVdsuTvz8pLqoTEFWcwIDahvgDxrRDn4RVJNcEW8tbw0vI0yScVqZbOBk7poPoRCcbYEOQvdYs28qBj+Fwi0cSBRP9LnUNxH9uwBeTdeuAF7JBe4kq5tKNQf8F5Rln4g+aPVJwLn8nYNnyR6htaTv19Pe2eeetu9CaxrdnDWnkfCSUBYG15N1dTdO3PsSYm6ch1DE5EH1zes84eOyqH1zopyA1GtICHoVsrm79uD3uDpQu/pAWwzH/p+ptsu0I0vFH7ZEciwiT5Ooj1G9Gbmvm2dC/fyIsHtIOzZmwv03G+g20/v8b1hQ2g6EM1SraP5dO2D7wSSn7TnyaEWsUwyEMKA/A64UCPyXk4nKQvdYs28qBj3PPYetBnw4bLQLb+Y2gexRIfe3X8Bl4POWmddX8cIC137q/nuxYsLoZhYSoMdYkYtcxDV7tjmo4fgu/crPtfXeBlb5as7bvoG0A7XcocJFSVh2BW7S93uS9M20v0mLvN5U6oo1Ckc1UhxyTmCLwBI4nxkMW8SguE3yhPdSJOZV1pd4I8PlMflJ4kponNbxBGz14lGIQxyFStNU/pxjVmRUoPC3FEq13wisTEPtor8nzDgdlLF+TQWM5dCYdJ82NJ9iw/5D1gDUPhKp8HaoX0e8GBWjhhVL15DoSAfQN0RjvegHBBLC6Ki/ej4q5VEiRkXIro86DBhQhnlecZEMv/BqFPGAO9TnShJtTMUtdKt3yxVIi+bM+ZdDZlbZidIfPqe6dcCJPvFZp/roKWbVNcwQyFTbBXJOJSl+FSNLdGhaouda/mDo6h9Itjlqe6phA63x/7F3hg4jNbVUU3CuvBW8B8fJ0xHRZtSjUpJlKKSvHFAI7l3yc791oOvGXTOzG7VwntgeH+HXHrne+UoddqgTumjHIe/VH4T9W7GnJGlKwhJQzBgcWPTENcOLrMqWzQUisWQL/H9u2VO1wkWkMSKa7gM+DePT6N0uNC5QL09picE83Qlux3XZtVcR7mK4R1l6dfGHi/U2MhwYJRb+20hhWgptoF1kie4SUMwYHFj0xLNclRSC2cefPRPmoxh3iZFMAvMg33zu2ZQOV3leozlcXedFmYBGXRRoyTCIMW+HY5BY2dTiJsBnDK0zFd1aqcK33lnCl1nz+y2yrqqXKWbpFcj0J5pFH+xb0BCVnySw0Owl09qsEcqGKH2hNcp08H3TqPq3MrMsvcE83Qlux3XZSkzqv6cChjlmAA3OC9nsSuJy6G6R1DvpZzpaNdL3uv150a10InNPHHdAMNB/1Y/2rbEXvq/bjz0ASZ/4VcVMeE3f1TENFYfHw/cyNHZnzc4YdqO/f9sPY5LHvN/L4Eol0cSxjhwRwLkwhrtVXFZ4RbYnzdhuA5Q98USzAJP56AhtNgXELhIaw9XhRRJcwdYxZcIg/OVYgBPLebbTrBUkRrWvOIPNCruPxl9STOesLEEclJeWBK/A8bINN+l91y7xegdS5xT5J726HMgDbag4pdrf4C/US1qS4gqGAk4wdHVl0OfjWzsdxSyyTJYue2FzOCyxpSCGakiaCA3Or++3HT4rclbaURxV/+fhfPOfusMW0x8DYO6ZvKZZyXrhM3UMae48XvfqzTZ3+S2K6sFlc1j8OgbdU14fKpeMnOZv8DEfZ00Pf1gNpNIuOUqIE1soqAg1tNQTrKIcZHGFPGAWz/5cx/A5BkoV15x3nfIsamSQxlUJJNMW2LQIDzelFcLqElDMGBxY9MZzvQH+wcSdq+4qqttK200ztetNnvUugEZ2ntmdytpZiaimNDEiJ0PnHH84opWbyBzbFYptt9Dp6URtXXyL8ndT0Sf4i2RIN7WmB6gp8BvmmZy7X9nzs8YWytprOyigpX3ySxrbFv/FCR3HQRZJ4/lkoNJiOVI8T8I2BxW9McmKi5mvT52tkJOBoOR26BKCga/saIbymARt+3x8iT8HJssapqj5lhgCblPSq7o+zNrBSbHHIlRfdFQn6pU1BoJlX87NUoEE17V+7VZjJDziDLJhIeEOByWnBIE2uV3ND4sqxmgBBZsbEs5B3RmtBJO93sEGwnno3PYhy6YzhL4qznqNEbbUejN5KXWtxgBEJA3VuhhDJ6QxGcdkDD1EDItXx5aKTLahBE52QlRHfpyGE73sAAVmVxoXYPxu4ujRKmpio5YjURjJqq0MMUph5N1yfHjodwISN6qCvSMjgzgx71xuovmiMySHzzMTBAV1sp3Ltx8TlbLHoGUH/u4UweI5u1rv/vI91g6jcTjuHt/IBrmrqlrWLIec6ELGgN/n42jNWczI/fwrhe0r+Fd+ya26WwqWd72udpemmHR7QERSZO80CPRkWIh1b/Peu/3LBmtGn7FRUO+8gcwgeXAKZJNiKeFzSbQkbbRGiz8BDCQYhsHGuhzHGCnCGHmkU1jXjctpfecgjada579QdPFdnxNWKgLAkhSm+UnQG88eLcATR9PDN1WQVIR+pMEDRj5qd7CYLT9I0PWwUjpZqKTvfkw+egrzdgjhMWj9/0heA30uEVUjyiQrJ52DazA50W8X590niDgdlLF+TQWM5dCYdJ82NJ1gHVy7PGZNNhKp8HaoX0e95g5I78qy6aqe2I/HrjlhYegHBBLC6Ki/ej4q5VEiRkXIro86DBhQhnlecZEMv/BqFPGAO9TnShJtTMUtdKt3yxVIi+bM+ZdDZlbZidIfPqe6dcCJPvFZp/roKWbVNcwQyFTbBXJOJSl+FSNLdGhaouda/mDo6h9Itjlqe6phA65B1dDTMmFXy/kb95r5yyznD7LWQs+TXcvyaFhdtoA0vWRCXRxS+AvKRxRO5Nl4sNe4z/l6zOMQ1K8lY3yxGX48JXywipA0+Kwjv0NjgnWm71VJaQaigJtEaWM1rIqxgBbuOH4IqCkGyeujcHhxXmZ7ZGzL825lvxXAdC0SxjXnFaARMcIUkbYfIze7UQseXQjUGMj5VqDU7NFjT5Bt2wQUnWzDY7Jdo6LdEkquB++nwL+LJfHI2KaBl5Z+q3vwWsRfe8bHavNUH0HYynQanVI5bxmuSCj3WDT4z7wom2Enn7cj59Jt2IeEA2++vbByRHN5+Boj8/a2rP3FQYyf3RehPtyWiyByJQJffmg03Hq5ABzSCrrIpb+MKs8Im6692o7ngnmYItKjSdbe4I442JDUyib55g90D5KspX6Nu/pgmEjnMeOiKtyNUQjKS4eXziwlxhB1lZoHVbnhwLAV6SJTv+HId/7Orut6ViAH114V1hmOPhGktRIk2gSoVWezc2QN5paM/cuGiyzUU/QKEftjYE+zzKytKKSQ+KPpzDLfXEvASyfpQJC0rCmBnASph8aCc75Yqy3Fag+aXY6ZRmVsU6mWWL/WHBlt9mia+1PEfw30VgToEWEBegdS5xT5J7xyLCJPk6iPUE/wMkcoI/9V1BcOU2OiYre+wUQXGQVSPSyyTJYue2FxTQYlnkb62QUjNf20BRHckjiJUAsALRHa8yOQzjMaDFtIEj3cHIf9QEG1MQ72nkeIOFu3AvMjJxynjnaQTzTNEQagMUA5Wc1zoDGpQctOnEeMo7riV1GAUXoHUucU+Se8WtuJ1DbueGNBjxQhBn1U+ULn3Cexrdj/KpeMnOZv8DEfZ00Pf1gNpNIuOUqIE1soqAg1tNQTrKIcZHGFPGAWz/5cx/A5BkoV15x3nfIsamSQxlUJJNMW2LQIDzelFcLqElDMGBxY9MZzvQH+wcSdqW0a/03s2Ao8nc3EdcH5hd4CiKu/NG74KeDVQnurI3NBY1tPiKVBbpkiG63ZB3wZzgXBtFXnVXpveD/Sd1SCOj5Yj5fhcnfZLQSw6HL9iL9TaCHfogZozAwcpkQwCPwE7nUlkt2CY0do0RX5zmfB17i2APC+xoFEH14JL1/NumT9NAtThY9nyAu7iuYCLSykUPxdIwITcVIlneoXXQwlMORwAzLLEG1ffObqzfuWhsRvI65i/lnWTXZ8Id/NnOikbrR0CjQi5TVOGShFDo5LzW/1rjxKjfdvhpeO+KiBzoBMdjNFPwGaqDOmfu/TVV0hCG1gaQTHxQF+53GBiUDl/1XRvEv2eNPufgB6hVSFDaxX/lzH8DkGShX9X7OoXuVhEsIR4sOtjo6R3274MdJusgms4oQsSXctSMxZhVRwDq7XBnMt4IWXSJShl9AgPzVdKGtICHoVsrm5hjUQtfRsFqXNm1TTQGzpLu1Q27y6w0HURtRUt7otMS04r21+kMnxP+n3sNriO34dMXt9YoPytXDJmkhgzczDaY+h8wpQz7jcLoSu4N9KcTwtqZu91pO0J2SU0wEh/hXj4c7UorYme9BuRuiz552YUKrCfaqPboNMjDWDVhMBDZaoU4SnEbJGsYKEqfvh0A2JyrkV+33FonLYh92uCdYGp6vA0evzO5MD4Sj7fLKiRkAhnGnGURt7LFQk564e/grR9dYWJzOdoKLbQvzfr8V4xsuvNnNnZqidlHDKaknwiBtu0MJ0bRacVdmGWlYqmHRhl/idbXdAxkC2APC+xoFEHVWGTACHNMEwsnWBVa849b0bRcTzzSsxgsYBcDHOvMuU34uCwLbxGvDjWYblmH9x6CtjTCHWkXRSMKJ0TS8sLOr++pfOqSXfW4HqEtdWG9f6P7+o40B5dQ9oId+iBmjMDNqsem9HiRHK0u/JeFCp4D2UkKwkLIPXl5n0PA62CV9faw5t2G01lGKiCgifLF1K+HTxXZ8TVioA/011ILjN1flgScreCNPAJytqHAsg+N+s279xZt0cTr44nZk4Tg/WCQqZqorXulXXOcQUvTt1jfI2q4PVxyXh+ZA1l8Mb8yWIITtXsSmw4nQQf8joAB8lANUyMO7JvU57+Rv3mvnLLOcPstZCz5Ndy/JoWF22gDS9ZEJdHFL4C8pHFE7k2Xiw17jP+XrM4xDUryVjfLEZfjwlfLCKkDT4rCO/Q2OCdabvVUlpBqKAm0RpYzWsirGAFu44fgioKQbJ66NweHFeZntkbMvzbmW/FcB0LRLGNecVoBExwhSRth8jN7tRCx5dCNQYyPlWoNTs0WNPkG3bBBSdbMNjsl2jot0SSq4H76fAv4sl8cjYpoGXln6re/BaxF97xsdq81QfQdjKdBqdUjlvGa5IKPdYNPjPvCibYSeftyPn0m3Yh4QDb769sHJEc3n4GiPz9ras/cVBjJ/dF6GEytStSr5wQ0HfAKTvw9n3OwrVbfOob8XvLDWfeq3Q/WHM/DN/Vfja+I65oEZ7/qajKHaO+oBLQ477B2XYjv/61IEVsmvNiykw3O7GDoMD1O3+mWpLEBFCNrnypIomZvEVxWLLQqksMWW5JbRiieuUOdFvF+fdJ4n6Ihi20TAte20AO0QelKJxMzVD+FMQ0wjr3WEE2OgT9Jo4BFCTfU/PwnMrd49hC7NAVRcz8+6osMsY+vxnPQ/UDXQpHSHPlJGchAH4KPNLz5S4YJFOPa4aUKr2V+SABFr9h1YQofD38T48UF4kqnRByA68EPINXtV6B1LnFPknvFrbidQ27nhicKVpY6m/u8wnmZhpxoiB4xHpHa0LK+QYtAtv5jaB7FMMgDHLcy1Iy9xt358PqekkEdo/38l3J2fZdCiipz8EZb1kS+Pq+5SvWpPFYh/X1E/7EsLVPNSnN7zyW2Et794flBWWPyyU2fJUR36chhO976wNNLKedv5rBT4SliM4roMJue309RKtGDhIBd2WnPmlyqYCg+B5PqZoAQWbGxLOQqqXqcoD4deyfTkSnbS22NznqrT4z8g+ynBHWefztMreIAav3TlDdlH9X7OoXuVhEqgtJ+/S2pD181VwS1oJvlabtGO2PKeqTLSiasbhaoqAIxBVLr8v4AH7mjKVdSC3g9qs47sJo484xODtuKQFisfcbd+fD6npJ6ZSjcfUCKYg7D0aeuYOSYnIro86DBhQhsl5j0U3l9SZ4ZPs5+zIbkmN8X+p4SBHwHqLjGQtq8DqgwtOxukIFS9/Do110wrhJtiXfw0QfP4dnDWnkfCSUBYG15N1dTdO3BYE6IhJ2JL/WSmYZLl374pHzwayb9G1rHlkemJEKyYwvyJIUSe7AzfhKPt8sqJGQ47zZc2Xte2H4yZVC2OPqKhcFM70W0Gg/twoWnAlnCm2P/0491En0e/jLw3FEamUGfKdHWmni55AUBCR6of19hsKWKt51xmk4ufzvukbhMMAglY6TLG5ujivJWN8sRl+Px+0nrPfPRhxlCf5Vv8UoE+88lthLe/eHn3dcYNJAuguGeBBMKsr7YRrSAh6FbK5uYY1ELX0bBalzZtU00Bs6S7SDtCm7YC4D1RQyW3Q9/kf0J36/WYlCsAkSGwcOsDe26SA/EGXbh4PNa98QTSl5Ef0qQSsfw71vjtGxTSNSKTqW0dzVscI9cFhATou6jKmTe5OvXIUTHBLgLrQLlkCSBxxbXxMjCUsL0C8+VNI5CXp2Gz8B1aMYH/CDFzn0JcE+Qk+3FCP9KU2enLR2D6L7vSD3zpUi6NwnvZvdtMTaciW20L836/FeMbuifmMOLRwH0mGWZbr8rZUMMcYzRsjjqmAi6hJ4BrpkM5stDo4p+L5SKU61j4q848+1nlBkH/qda2L1lNiGIdY34uCwLbxGvMKnkLMT0H+2cDNRXOng8qNGFQSqoEklWJb1VY8EQYNLFkFQCufzBMYTaZ4Hk0qZKIRc1Rqp102x1DLZfHZhKvGQCtGNwLy4MJAWwzH/p+ptToN1oNEhgAzk4EMlYME35QEpvz4ntaz2M589elakQnY1gFqrXrRROhi3arJ4ZJa5C0CthJCYYqBNRPARpAS2eKCZLc+ZaDTlMlsUT1E8s9WQFsMx/6fqbbdlRFTfxj6XzlqRmJsyqBPT0VM5cs6MgPq8+92TVYjXO4qW8yCyueV3aSxYDQ/OEu/lnCymdMFsPh5+9UPacjWTEiRqw4mymnHW0MPFNs56l/Fjsu3XJJ9UrSRzUkafOuPIcP0vGjRHexJpL/rkOAWz45Ov4wJi+QhmkrBLluxql9+aDTcerkAHNIKusilv4wqzwibrr3ajueCeZgi0qNJ1t7gjjjYkNTKJvnmD3QPkqw5Mf/t3j6vHGe3Lo5PaJskTarwi/sBNaF94XDrUwOuEarmphh8Nvu/4ch3/s6u63pWIAfXXhXXAhHi0KGyRUlAo9wHNLNy3M1tve8jUzLEW2uJrTbFbMpgCGilo04KZnt4DVIyaoy8wt1zEj6jkkgBalW62QVf9S90jYpr0rgI/2g63X596PVpALJQNZCkgFJ1WZp9ZQqTCPmuAPW3jfh0/vnOIjv3GAMoOiiv7+LNrcYARCQN1bkYqfYlcd6J2OQNoHClcqbQm7WeKGSXv5o62hEZQpNUWKbbgsvBYDD61Sy6suLVGX+jpu6AKOiJj0DpnhN48Dhwt5BemdNGE4DBywLUOlb2xxQ8MWUcVnmxxyrG2OYef+Ri+oWbfmH9wa2APwkDrWcKLgo213MFYe2b7iOsdj9ru0dGwdageVVV9yoD3tAo407LRlK2S6gPhG1gaQTHxQF+kytgJ6ofRE5M4kkGbWJT4z39boh7sySJ556270JrGt2cNaeR8JJQFRIV6pStr3gOx+jGTFGDTZoI9raabwcLV0dGwdageVVVjsMlZGl7JAuiJx0O4AXYVhJQzBgcWPTG+9RWA3JuZaMd3XeiBBMpN+4qqttK200wDhwlYF7mb+Su2zX5xZrafwpYq3nXGaTjhD6/8ESY1b4nhHSS8IbHS/6tuSELMFEHBMgH61BbshkznI/JDBV1AeLKQ7IUSD/uE3rWGSpV9jXKsPT+Wf//9M+Ax9QkzSSLNgfPm5eMYONNaHtvxnedzEqsWYqeA4WD0NgaLUMSjbYLzcRGeDV26epvKCTKPmeI6sBq5aTrrh0jI4M4Me9cbKDSYjlSPE/DEX/61hUfvXwkzYAOQKodyhW49uKJG5k+2IfdrgnWBqerwNHr8zuTA+Eo+3yyokZBgWpEh3JNxpwycNxcuJvzb/WuPEqN92+FS+SCBvFr+KmBt1w2waracpjxhVF7y2ed2n4ZtdHF4WB1QNadPYaRoM+Ax9QkzSSJgbQIAt09pp7tXWlsKnP9bgzNiA6klWaJlvaE9M47X2kSFeqUra94DSmNMILIxJD3aCHfogZozA5tQKDtTns4+czamtL9bHiic1fcLlWIuHrx7tiVnHCJ973f0lD1GpIxrcYARCQN1bl977bxpCGi2494v2kL3kM0qFZGMrgNdjxsS51rA1/389Cd+v1mJQrD72114UlKPfY6ASpigGKni8Ty04T1XULIbTp5otPVa16YjDv8toeQt0heA30uEVUjyiQrJ52DazPA19gpV8RRa7CUG6dJKwnqwbsSiwPyi9eqfSVjxIJfcBgKakx4hmQdmJ8aTjnUdFXYbPwHVoxgf8IMXOfQlwT7BWsMqdo43wp6ctHYPovu9VPVKZaR4z3c22xAUtl8g7bbQvzfr8V4xHIsIk+TqI9TEU+SfjfGsJjWjEfF09GNDCeZmGnGiIHjEekdrQsr5Bi0C2/mNoHsUq+CRTgTzNuBXbqOQ4OM207nWv5g6OofSrak2BVyqJaMPOkIQPaVmd+b8DQpZSxd01sIYAdOkGuiaxBh6PflUtgS/SenpnNk9N+LgsC28RrziSKVPCzt431uSDzVWfOcdOQNoHClcqbQm7WeKGSXv5o62hEZQpNUWKbbgsvBYDD61Sy6suLVGX+jpu6AKOiJj0DpnhN48DhwqauEiUfpQNcoAvj/+sbokgy7hyo0SOCbIMNaaQUaxy6stJluvvueMBWpUauFPgIuTcxaW+5jT2qnpOMguRG3CC+mlyyFNBNkPDa6IUTpYmGcLizjZZL59O8C3WenwgeqSX6UYaE5aWJoAQWbGxLOQZ2Q5tckuG/hFYpjXiWoRNCXVkXf771Lo6diW5LrNULzYCPSheznZJScFA5Lf8IRPLFGRWBNxOfdl56POxpQYWcWnoXXOzB4DvBUcC2trlqoZoKi7nDiaG5oAQWbGxLOQlV09326Y3HnlbylEWZlpnl0PQNgroYw9jturWTJLF4VPehSrfG91rDqq2ecSli64yAGYmUe0liRFjtmnOn4OE/22nK2iOmYQGnRyuO442sJ2ZivZemNwDSFlVNgGu02jpNIqfSUqMaqTH3LLk+EoCxKWWeg5cN8/7kzIuSMm4R8H4XoK5xrjEP5G/ea+css5EDpX5nE5rldr6LOhNsX956F4FxckiBccFwqcUi2VAGpQIT8xqhMygiNBFSaH2/JEuQYML9ZtYTzOsR2jICTl5rYonl9Hx1ydHNCEyA2QgUH6deAFvX9t6yJ4/tPHjiPirS04TyJVuvmhL+wCtLau+LGBZoDN2qBkC8GMl1SLHo5SJmgmaCvm33Wn5fLFG0CgFEsf91K2jtWh91ipomyIAsOAOifCFNBI0g+5iYI38lKX6kMGO9IYypZBkrEwqlFOrNt0vJi7zc8HwwNzhl8zsRvfiZHiOEm0RPXcUYck3M2O/Ma1Qdh5ae4YA9LjcKDxTqrHq1PqbCMZO6p1cL7EhgOCzMtA7QtALy7r/wKWxvmWDF5459Gy8d8fIk/BybLG4YbbFVNb3GBSFG6WbaA3TG6HMgDbag4p7B65QqRWNkOvUmk0KBVqTSKUPwt2XTzR6InHQ7gBdhWElDMGBxY9Mb71FYDcm5lox3dd6IEEyk37iqq20rbTTAOHCVgXuZv5K7bNfnFmtp/IQ5UKWk36sFjW0+IpUFumSIbrdkHfBnMmCipVotFfgpdxo29NsOwFliPl+Fyd9ktBLDocv2Iv1N8ZTR6PBTJV06QEHnbkXUmdSWS3YJjR2iwUAg3Yi1LtbdPGNruyMiqc1fcLlWIuHrx7tiVnHCJ973f0lD1GpIzlGWfiD5o9Uqzi7nk5bL+kgbXk3V1N07eg6pbJtFFxQP24Pe4OlC7+21V//O/qMoPVQ0//NERMmuQrAxOGAXII3xlNHo8FMlWfgSVnCIj/PXLLo5117p1+fKdHWmni55AUBCR6of19hsKWKt51xmk4ufzvukbhMMAglY6TLG5ujivJWN8sRl+PNQXor3tsSrAtR9da3nlEteWmddX8cIC137q/nuxYsLqMB5rg0hmfALpG4/9ToXI/tv6QC02ZQVL6IoHgESQPs+x3r5EqMoBznjgsDCkH+tN4MeNNhB5oxs+JrM0MjfKeCWZy60nUx2bgLrQLlkCSBxxbXxMjCUsLxZGyJdd06ZUOB2UsX5NBYzl0Jh0nzY0nwVrDKnaON8KenLR2D6L7vceldORBFAymdmGWlYqmHRgez9QNdS1mjVduo5Dg4zbTuda/mDo6h9KtqTYFXKolow86QhA9pWZ35vwNCllLF3TWwhgB06Qa6JrEGHo9+VS2BL9J6emc2T034uCwLbxGvOJIpU8LO3jfW5IPNVZ85x0QbQAUOEpKB5GOsvH+Xf9j3Hhhjy38YbQX1RSypdprCBjgnxKRYtED/kb95r5yyznD7LWQs+TXcvyaFhdtoA0vWRCXRxS+AvKRxRO5Nl4sNe4z/l6zOMQ1K8lY3yxGX48ey3+P/Zv9iAjv0NjgnWm71VJaQaigJtEaWM1rIqxgBbuOH4IqCkGyeujcHhxXmZ7ZGzL825lvxXAdC0SxjXnFaARMcIUkbYfIze7UQseXQjUGMj5VqDU7NFjT5Bt2wQUnWzDY7Jdo6LdEkquB++nwL+LJfHI2KaBl5Z+q3vwWsRfe8bHavNUH0HYynQanVI5bxmuSCj3WDT4z7wom2Enn7cj59Jt2IeEA2++vbByRHN5+Boj8/a2rP3FQYyf3RehhMrUrUq+cENB3wCk78PZ9zsK1W3zqG/F7yw1n3qt0P1hzPwzf1X42viOuaBGe/6moyh2jvqAS0PTCSkrj5rmEGdPKzjFrH5ul7VSqyvSdz155ZcIxt6VADo6ReZovLnRFcViy0KpLDFluSW0YonrlYkxv59rdLmovrQsV/5sxhbIw16PpzMYF/3tjCad5VWRIYMKglGCEeBMlJnA9iF0yNSFiocwxip/YyMXlAl1BFcmeFQL/tA/8Jdm03bGt72ixYc40w3WDs0d/RylOVQXXKrxIeorFA/6+5OoQC1lvR3dHoXjv7hLJyJkOQo6PYwLNnnX70Vg3VI2Hqem47k1CQU4hZo3ZqcrmZFsOQJBe3Td6FGYM6I90wm57fT1Eq0ZrcYARCQN1bnF96oDe3dydEqsWYqeA4WD0NgaLUMSjbYLzcRGeDV26epvKCTKPmeI6sBq5aTrrh0jI4M4Me9cblRHfpyGE73vrA00sp52/msFPhKWIziugwm57fT1Eq0YOEgF3Zac+aXKpgKD4Hk+pmgBBZsbEs5CqpepygPh17J9ORKdtLbY3OeqtPjPyD7KcEdZ5/O0yt4gBq/dOUN2Uf1fs6he5WETgejwIOfknx3zVXBLWgm+Vpu0Y7Y8p6pMtKJqxuFqioCPbdILI3oyStvR8bS4qPveK3MiJMsAqKSBYdaajLFhGNz2Uu1ozu0WALxej6CcFm8pyEN3LivRBzq83+Dd06cbVEitnFZL5RFqM+lNhfPnFPm2+j2hmptbdRvJHuW7+nMcSrd2Y85Hm76i07o9UAxN4ZPs5+zIbkhtYGkEx8UBfpMrYCeqH0ROTOJJBm1iU+M9/W6Ie7Mkieeetu9CaxrdnDWnkfCSUBYG15N1dTdO3oOqWybRRcUD9uD3uDpQu/rEEpdtOjicPvjEr/PFtcBzkKwMThgFyCNoId+iBmjMD+88oj8DKyeOALxej6CcFm3ynR1pp4ueQFAQkeqH9fYbCliredcZpOLn877pG4TDAIJWOkyxubo4ryVjfLEZfjzPgMfUJM0kiHsRx1geV7m52JoGtZ7z6+vfz7f2qDMwI7KofXOinIDUa0gIehWyubmGNRC19GwWpc2bVNNAbOkuBQckp+p0lKw+DeHZ7L/32qI7xp+RSKpoAttbCQ/yqMvYZt4kbmkHznjgsDCkH+tN4MeNNhB5oxsrl5z60sE49W8IQIb11wtxKC5cm+AM7tVXlfNABiuEVZsoNuLvujWtww/7OxMo+TVc1v19wMiobUjytJDRZ/fYESkjzjPHNynXz5+Y74/jllajyK4aYBvc9P/CQ6qNeZ/1tIq9EmqNBBc/b7zpi4bvY2FFIsKGdrhbmnHJ0VB4KBLKrSAwnBRd0OEwzEZv+S3WJLM8wy+6Jdp+GbXRxeFjVEitnFZL5RFqM+lNhfPnFPm2+j2hmptbdRvJHuW7+nMcSrd2Y85HmOxeycZ76bYOFPGAO9TnShJtTMUtdKt3yxVIi+bM+ZdDZlbZidIfPqe6dcCJPvFZp/roKWbVNcwQyFTbBXJOJSl+FSNLdGhaouda/mDo6h9Itjlqe6phA6+nweCnKTw7cCOVM14gTOmjMNklcd0dUeS9Qj1h5ro3JZyfNN6aORRkIO6JapN0rwRNpngeTSpkohFzVGqnXTbHUMtl8dmEq8ZAK0Y3AvLgwkBbDMf+n6m1Og3Wg0SGADNOIYTRATMX+ASm/Pie1rPYznz16VqRCdjWAWqtetFE6uJ4mmXd8ziltVcR7mK4R1l6dfGHi/U2MhwYJRb+20hhWgptoF1kie4SUMwYHFj0xLNclRSC2cefPRPmoxh3iZFMAvMg33zu2ZQOV3leozlcXedFmYBGXRRoyTCIMW+HY5BY2dTiJsBnDK0zFd1aqcK33lnCl1nz+y2yrqqXKWbpFcj0J5pFH+xb0BCVnySw0Owl09qsEcqGKH2hNcp08H3TqPq3MrMsvcE83Qlux3XZSkzqv6cChjlmAA3OC9nsSuJy6G6R1DvpZzpaNdL3uv+6OlMnpD/QnP2CxybbOPUKKNo74jHcmvdrR5MTdTsGR/2iX/kCMT5IFX8z3SnqxHf2PgaDokFnhy0ok+j2Pe1V28yXISdfN73UsIVi+ZOaV3afAS5TsuJnD+CYh59UtVw=="
    # s = "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"

    result = des.decrypt(base64.b64decode(msg))
    result = unpad(result, 8)
    return result.decode('utf-8')
