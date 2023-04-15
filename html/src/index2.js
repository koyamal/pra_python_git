const memoListItems = document.querySelectorAll('.memo-list-item');

console.log(memoListItems);

let colorSwitch = false;

const onClickColor = () => {
    if(!colorSwitch){
        colorSwitch = true;
        memoListItems.forEach((item, index) => {
            if(index % 2 === 0){
                item.style.backgroundColor = "yellow";
            }else {
                item.style.backgroundColor = "red";
            }
        });
    }else {
        colorSwitch = false;
        memoListItems.forEach((item, index) => {
            if(index % 2 === 0){
                item.style.backgroundColor = "red";
            }else {
                item.style.backgroundColor = "yellow";
            }
        });
    }
}
