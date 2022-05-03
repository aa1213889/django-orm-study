;
(() => {

    const apiUrl = 'http://localhost:8000/'
    const init = () => {
        initEvents()
    }

    const initEvents = () => {
        document.querySelector('#loginBtn').addEventListener('click', userLogin)
    }

    const userLogin = () => {
        const name = document.querySelector('input[name=name]').value
        const pwd = document.querySelector('input[name=pwd]').value
        if (pwd === '' || name === '') alert('Please enter value')
        fetch(`${apiUrl}login_user/`, {
                method: 'post',
                body: JSON.stringify({
                    name,
                    pwd
                }),
                headers: {
                    Accept: 'application/json',
                    'Content-Type': 'application/json'
                }
            })
            .then((res) => res.json())
            .then((data) => {
                if (data.code === 200) {
                    window.location = 'index.html'
                    alert('Login Successfully')
                } else {
                    alert(data.msg)
                }
            })
    }

    init()
})()