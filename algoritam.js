function fizzfuzz():
    n = 1
    for (var i = 1; i <= 100; i++) {
        div = 0

        if (i%3==0) {div = 1}
        
        if (i%5==0) {div = 2}
        
        if (i%5==0  &&  i%3==0) {div = 3}
        
        switch(div) {
            case 0:
            console.log(i)
            break;
            case 1:
            console.log('fizz');
            break;
            case 2:
            console.log('buzz');
            break;
            case 3:
            console.log('fizzbuzz');
            break;
        }
        
    }