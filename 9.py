for (int digit=2; digit<=9; digit++) 
    { 
        // if digit divides N then mark it as true 
        if (divisible(N, digit)) 
            divide[digit] = true; 
    } 
