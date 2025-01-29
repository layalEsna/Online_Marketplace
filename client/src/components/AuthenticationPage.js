
import React from "react"
import { useFormik } from 'formik'
import * as Yup from 'yup'
import { useNavigate, useParams } from 'react-router-dom'


function AuthenticationPage() {

    const navigate = useNavigate()
    const { username, productId } = useParams()

    const formik = useFormik({

        initialValues: {
            password: ''
        },
        validationSchema: Yup.object({
            password: Yup.string()
                .required('Password is required.')
                
        }),
        onSubmit: (values) => {
            fetch('http://127.0.0.1:5555/authenticate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'


                },
                body: JSON.stringify({username, password: values.password})
            })
                .then(res => {
                    if (!res.ok) {
                    throw new Error('Authentication failed.')
                    }
                    return res.json()
                })
                .then(() => navigate(`/sellers/${username}/${productId}/edit`))
            .catch(e => console.error(e))
        }
    })

    return (
        <div>
            <h1>Seller Authentication</h1>
            <form onSubmit={formik.handleSubmit}>
                <label htmlFor="password">Enter your password</label>
                <input
                    id="password"
                    type="password"
                    name="password"
                    value={formik.values.password}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                />
                {formik.errors.password && formik.touched.password && (
                    <div>{ formik.errors.password }</div>
                )}
                <button type="submit">Authenticate</button>

            </form>

        </div>
    )




}

export default AuthenticationPage