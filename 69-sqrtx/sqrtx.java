class Solution {
    public int mySqrt(int x) {

        if(x<2){
            return x;
        }
        double a=x/2;
        double b=0;

        while(true){
            b=(a+x/a)/2;
            if(b==a){
                break;
                }
            
            a=b;
            System.out.println(a+"-"+b);
        }

        return (int)b ;
    }
}