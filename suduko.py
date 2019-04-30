# [數獨](https://zh.wikipedia.org/zh-tw/%E6%95%B8%E7%8D%A8)
# 有9條直線、9條橫線、9個區塊 (81格)
# 對點(x,y)而言，他屬於直線[y]，橫線[x]，區塊[x//3*3  + y//3]
# 有9種數字，同數字互斥，不同數字不互斥，所以上面有9種
# 有81個字要填，如果已經確定的，填下一個，否則嘗試所有可能的
# 目標：填入81個數字，一開始已填入0個
# 因此函數的參數應該有（盤面、已填、直線、橫線、區塊）