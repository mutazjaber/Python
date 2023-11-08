// class Solution{
//     isLeap(n){
//         if (n % 100 == 1  && n % 4 == 0  ){ 
//         return  1 ;              // leap year 
//         }
//         else {
//             return 0 ;           // not a leap year
//         }

//     }
// }
    function isLeap(n){
        if (n % 100 != 0  && n % 4 == 0  ){ 
        return  1 ;              // leap year 
        }
        else {
            return 0 ;           // not a leap year
        }

    }
    console.log(isLeap(2021))


        
