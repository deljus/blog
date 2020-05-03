const alerts = document.getElementsByClassName('alert-close-timeout');

const delay = ms => new Promise((resolve) => setTimeout(() => resolve(), ms));

if(alerts.length){
    for (alert of alerts){
        delay(1000).then(() => {
            alert.classList.add('fade');
            return delay(1000)
        }).then(() => {
            alert.remove()
        })
    }
}


