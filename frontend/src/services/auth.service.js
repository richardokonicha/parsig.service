import axios from 'axios';


export const LoginUser = (email, password, alwaysLoggedIn='true') => {
    return axios({
        method: 'POST',
        url: `${ process.env.API_URL }/authentication`,
        data: {
                'email': email,
                'password': password,
                'always_logged_in': alwaysLoggedIn
            }
        });
}


export const UpdateUser = (tokenCookie, data) => {
    if (tokenCookie) {
        return axios({
            method: 'POST',
            url: `${ process.env.API_URL }/personal_settings`,
            data: data,
            headers: {
                    'x-access-token': tokenCookie['x-access-token'] ? tokenCookie['x-access-token'] : tokenCookie 
                }
        }); 
    } 
}