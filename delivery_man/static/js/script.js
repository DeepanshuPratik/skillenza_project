console.log('happy me')
var theme
theme = localStorage.getItem('theme')
if(theme == null){
    setTheme('light')
}
else{
    setTheme(theme);
}
var themeDots
themeDots= document.getElementsByClassName('theme-dot')
var mode
for(var i=0; i<themeDots.length; i++){
    themeDots[i].addEventListener('click',function(){ 
        mode = this.dataset.mode
        console.log('connected:',mode)
        setTheme(theme)
    })
}
function setTheme(){
    if(mode=='light'){
        document.getElementById('theme-style').href = "../static/css/base.css"
    }
    if(mode=='blue'){
        document.getElementById('theme-style').href = "../static/css/blue.css"
    }
    if(mode=='green'){
        document.getElementById('theme-style').href = "../static/css/green.css"
    }
    if(mode=='purple'){
        document.getElementById('theme-style').href = "../static/css/purple.css"
    }
    localStorage.setItem('theme',mode)
}
