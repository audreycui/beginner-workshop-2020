function getCat() {
    fetch("https://api.thecatapi.com/v1/images/search?api_key=3d61f12c-6803-4250-be69-ec2c2f5361ec")
    .then(res => res.json)
    .then(res => {
        const div = document.getElementById("cat-div"); 
        div.innerHTML = ''; 
        const cat = new Image(); 
        cat.src = res[0].url;
        div.appendChild(cat); 
    });
}
window.onload = function(){
    const catButton = document.getElementById("cat-button"); 
    catButton.onclick = getCat;
}