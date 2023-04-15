const memoListItems = document.querySelectorAll('.memo-list-item');

console.log(memoListItems);

memoListItems.forEach((item, index) => {
    if(index % 2 === 0){
        item.style.backgroundColor = "yellow";
    }else {
        item.style.backgroundColor = "red";
    }
});
