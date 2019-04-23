def transpose(a) :
    w = len(a) or 0
    if(isinstance(a[0],list)) :
        h = len(a[0])
    else :
        h = 0
    if( h == 0 or w == 0) :
        return []
    
    i = list()
    j = list()
    t = list()

    print(h,w)
    for i in range(h) :
        print('i',i)
        # t[i] = []
        for j in range(w) :
            print('j',j)
            t[i][j] = a[j][i]
            print(t)
    
    return t

def main() :
    a = [[1,2,3],[4,5,6]]
    b = transpose(a)
    # print(b)
    

main()

# function transpose(a) {
#   // Calculate the width and height of the Array
#   var w = a.length || 0;
#   var h = a[0] instanceof Array ? a[0].length : 0;

#   // In case it is a zero matrix, no transpose routine needed.
#   if(h === 0 || w === 0) { return []; }

#   /**
#    * @var {Number} i Counter
#    * @var {Number} j Counter
#    * @var {Array} t Transposed data is stored in this array.
#    */
#   var i, j, t = [];

#   // Loop through every item in the outer array (height)
#   for(i=0; i<h; i++) {

#     // Insert a new row (array)
#     t[i] = [];

#     // Loop through every item per item in outer array (width)
#     for(j=0; j<w; j++) {

#       // Save transposed data.
#       t[i][j] = a[j][i];
#     }
#   }

#   return t;
# }
# a = [[1,2,3],[4,5,6]]
# r = 2
# c = 3
# [[a[r-j-1][i] for j in range(r)] for i in range(c)]