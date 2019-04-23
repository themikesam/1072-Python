# 學號：104213069
# 姓名：覃融亮
# 作業八
# 題目：翻轉陣列
# 題目解說：https://moodle.ncnu.edu.tw/pluginfile.php/996243/mod_assign/intro/%E7%9F%A9%E9%99%A3%E8%BD%89%E6%8F%9B.pdf

def flip(a) :
    r = len(a) # 從陣列長度得知有多少 row
    c = len(a[0]) # 從第一筆資料長度得知有多少 column
    '''
        以其他語言來解析，較易理解
        for (int i = 0; i < r; i++)
            for (int j = 0; i < c; j++)
                ANSWER = a[r-i-1][j]
    '''
    ''' 
    a = [
            [6,5,4],  <== second loop of r 
            [3,2,1]   <== first loop of r 
        ]
    # first loop of r:
    ANSWER =    [  
                    [3,2,1],
                ]
    # second loop of r:
    ANSWER =    [
                    [3,2,1],
                    [6,5,4]
                ]
    '''
    return [[a[r-i-1][j] for j in range(c)] for i in range(r)] 


def rotate(a) : 
    r = len(a)
    c = len(a[0])
    return [[a[r-j-1][i] for j in range(r)] for i in range(c)]

def Main() :
    r, c, m = map(int, input().split()) # 分割三個字串，以int形態
    ans = [list(map(int,input().split())) for i in range(r)] # 依據行數讀取，預設以空格分割成list
    operation = list(map(int,input().split()))  # 存取動作到list

    '''
    以PHP的角度：
    switch ($val) {
        case '1':
            return flip(ans);
            break;
        case '0':
            return rotate(ans);
            break;
    }

    什麼是lambda : https://openhome.cc/Gossip/Python/LambdaExpression.html
    '''
    for val in operation :   
        ans = {
        '1': lambda ans: flip(ans),
        '0': lambda ans: rotate(ans),
        }[str(val)](ans)

    print('-----')
    print(len(ans),len(ans[0])) 
    for val in ans :
        output = ''
        for value in val: 
            output += str(value)+' '
        print(output)
Main()