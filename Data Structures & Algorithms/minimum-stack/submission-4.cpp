class MinStack {
public:
    int arr[1000];
    int minarr[1000];
    int first;
    int minfirst;

    MinStack() {
        first = -1;
        minfirst =-1;
        
    }
    
    void push(int val) {
        first++;
        arr[first]=val;
        if(minfirst== -1 || val< minarr[minfirst]){
            minfirst++;
            minarr[minfirst]=val;
        }else{
            minfirst++;
            minarr[minfirst]=minarr[minfirst-1];
        }
        
    }
    
    void pop() {
        first--;
        minfirst--;
        
    }
    
    int top() {
        return arr[first];
        
    }
    
    int getMin() {
        return minarr[minfirst];    
    }
};
