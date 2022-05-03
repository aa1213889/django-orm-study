;
(() => {

    const apiUrl = 'http://localhost:8000/'
    const init = () => {
        getUserList()
        initEvents()
    }

    function getUserList() {
        fetch(`${apiUrl}klw_order_api/`)
            .then((res) => res.json())
            .then((data) => {
                setUserTable(data.msg)
            })
    }

    const setUserTable = (list) => {
        let htmlStr = ``
        for (const item of list) {
            const { name, age, email, size } = item
            htmlStr += `
            <tr>
              <td>${name}</td>
              <td>${age}</td>
              <td>${email}</td>
              <td>${size}</td>
            </tr>
          `
        }
        document.querySelector('#userList').innerHTML = htmlStr
    }

    const initEvents = () => {
        document.querySelector('#addUserBtn').addEventListener('click', getUserForm)
    }

    const getUserForm = () => {
        const name = document.querySelector('input[name=name]').value
        const age = document.querySelector('input[name=age]').value
        const mail = document.querySelector('input[name=mail]').value
        const size = document.querySelector('input[name=size]').value
        const pwd = document.querySelector('input[name=pwd]').value
        if (pwd === '' || name === '' || size === '') return alert('Please enter value')
        fetch(`${apiUrl}add_user/`, {
                method: 'post',
                body: JSON.stringify({
                    name,
                    age,
                    mail,
                    size,
                    pwd
                }),
                headers: {
                    Accept: 'application/json',
                    'Content-Type': 'application/json'
                }
            })
            .then((res) => res.json())
            .then(() => {
                getUserList()
                alert('Add Successfully')
            })
    }

    init()
})()