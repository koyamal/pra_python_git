const memoListItems = document.querySelectorAll('.memo-list-item');

console.log(memoListItems);

// let colorSwitch = false;
let colorSwitch = 0;

const onClickColor = () => {
    if(colorSwitch % 3 === 0){
        memoListItems.forEach((item, index) => {
            if(index % 2 === 0){
                item.style.backgroundColor = "yellow";
            }else {
                item.style.backgroundColor = "red";
            }
        });
    }else if(colorSwitch % 3 === 1){
        memoListItems.forEach((item, index) => {
            if(index % 2 === 0){
                item.style.backgroundColor = "red";
            }else {
                item.style.backgroundColor = "yellow";
            }
        });
    }else {
        memoListItems.forEach((item, index) => {
            if(index % 2 === 0){
                item.style.backgroundColor = "white";
            }else {
                item.style.backgroundColor = "white";
            }
        });
    }
    colorSwitch ++;
}

const onClickLogout = () => {
    console.log("Logout Done.");
}
