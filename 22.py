int main() 
{ 
    int arrl[] = {1, 2, 10, 5, 5}; 
    int exit[] = {4, 5, 12, 9, 12}; 
    int n = sizeof(arrl)/sizeof(arrl[0]); 
    findMaxGuests(arrl, exit, n); 
    return 0; 
} 
