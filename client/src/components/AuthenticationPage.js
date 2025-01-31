




// import React, { useState } from "react"
// import { useFormik } from 'formik'
// import * as Yup from 'yup'
// import { useNavigate, useParams } from 'react-router-dom'


// function AuthenticationPage() {

//     const navigate = useNavigate()
//     const { username, productId } = useParams()
//     const [error, setError] = useState('')

//     const formik = useFormik({

//         initialValues: {
//             password: ''
//         },
//         validationSchema: Yup.object({
//             password: Yup.string()
//                 .required('Password is required.')

//         }),

//         onSubmit: (values) => {
//             fetch(`http://127.0.0.1:5555/sellers/${username}/authentication`, {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json'


//                 },
//                 body: JSON.stringify({username, password: values.password})
//             })

//                 // .then(res => {
//                 //     if (!res.ok) {
//                 //     throw new Error('Authentication failed.')
//                 //     }
//                 //     return res.json()
//                 // })
//                 // .then(() => {
//                 //     if (productId) {
//                 //         navigate(`/sellers/${username}/${productId}`)
//                 //     } else {
//                 //         console.log('Product is undefined.')

//                 //     }
//                 // })


//                 .then(res => {
//                     if (!res.ok) {
//                         throw new Error('Authentication failed.');
//                     }
//                     return res.json();
//                 })
//                 .then(data => {
//                     console.log("Server Response:", data); // Log the server response
//                     if (productId) {
//                         navigate(`/sellers/${username}/${productId}`);
//                     } else {
//                         console.log('Product is undefined.');
//                     }
//                 })





//                 .catch(e => {
//                     setError(e.message)
//                     console.error(e)
//                 })
//         }
//     })

//     return (
//         <div>
//             <h1>Seller Authentication</h1>
//           {error && <div>{error}</div>}
//             <h4>Username: {username}</h4>
//             <form onSubmit={formik.handleSubmit}>
//                 <label htmlFor="password">Enter your password</label>
//                 <input
//                     id="password"
//                     type="password"
//                     name="password"
//                     value={formik.values.password}
//                     onChange={formik.handleChange}
//                     onBlur={formik.handleBlur}
//                 />
//                 {formik.errors.password && formik.touched.password && (
//                     <div>{formik.errors.password}</div>
//                 )}
//                 <button type="submit" >Authenticate</button>

//             </form>

//         </div>
//     )




// }

// export default AuthenticationPage




import React, { useEffect } from "react";
import { useFormik } from 'formik';
import * as Yup from 'yup';
import { useNavigate, useParams } from 'react-router-dom';

function AuthenticationPage() {
    const navigate = useNavigate();
    const { username, product_id } = useParams();

    useEffect(() => {
        console.log("Component mounted!");
        console.log("Product ID:", product_id);
    }, [product_id]);

    const formik = useFormik({
        initialValues: {
            password: ''
        },
        validationSchema: Yup.object({
            password: Yup.string()
                .required('Password is required.')
        }),
        onSubmit: (values) => {
            console.log("Form submitted!");
            fetch(`http://127.0.0.1:5555/sellers/${username}/authentication`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, password: values.password })
            })
            .then(res => {
                console.log("Response status:", res.status);
                if (!res.ok) {
                    return res.json().then(errorData => {
                        console.error("Server Error:", errorData);
                        throw new Error(errorData.error || 'Authentication failed.');
                    });
                }
                return res.json();
            })
            // .then(data => {
            //     console.log("Server Response Data:", data);
            //     if (product_id) {
            //         // navigate(`/sellers/${username}/${product_id}`);
            //         navigate(`/sellers/${username}/${product_id}`);
            //     } else {
            //         console.log('Product is undefined.');
            //     }
                // })


                .then(data => {
                    console.log("Server Response Data:", data);
                    if (product_id) {
                        console.log("Navigating to:", `/sellers/${username}/${product_id}`);
                        navigate(`/sellers/${username}/${product_id}`);
                    } else {
                        console.log('Product is undefined.');
                    }
                })
                




            .catch(e => {
                console.error("Fetch Error:", e);
            });
        }
    });

    useEffect(() => {
        console.log("Form errors:", formik.errors);
    }, [formik.errors]);

    return (
        <div>
            <h1>Seller Authentication</h1>
            <h4>Username: {username}</h4>
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
                    <div>{formik.errors.password}</div>
                )}
                <button type="submit">Authenticate</button>
            </form>
        </div>
    );
}

export default AuthenticationPage;