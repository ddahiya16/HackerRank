select n, (case 
        when (N = (select N from bst where p is null)) then 'Root' 
        when (N in (select P from bst)) then 'Inner'  
         else 'Leaf'  end) 
        from bst 
order by N;
