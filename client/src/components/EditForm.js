

import React, { useEffect, useState } from "react";
import { useFormik } from 'formik'
import { useParams } from "react-router-dom";
import * as Yup from 'yup'

function EditForm() {

    const { username, productId } = useParams()
    const [product, setProduct] = useState(null)

    useEffect(() => {
        fetch(`http://127.0.0.1:5555/sellers/${username}/${productId}`)
            .then(res => {
                if (!res.ok) {
                    throw new Error('Failed to fetch product.')
                }
                return res.json()
            })
            .then(data => setProduct(data))
            .catch(e => console.error(e))
    }, [username, productId])

    const formik = useFormik({
        enableReinitialize: true,
        initialValues: {
            name: product ? product.name : '',
            image: product ? product.image : '',
            description: product ? product.description : '',
            price: product ? product.price : ''
        },
        validationSchema: Yup.object({
            name: Yup.string()
                .required('Name is required.')
                .max(20, 'The name must be shorter than 20 characters.'),
            
            description: Yup.string()
                .required('Description is required.')
                .max(200, ('Description must be shorter than 200 characters.')),
            
            image: Yup.string(),
            
            price: Yup.number()
                .required('Price is required.')
            .min(1, 'Price must be greater than $1.')
        }),
        onSubmit: (values) => {
            fetch(`http://127.0.0.1:5555/sellers/${username}/${productId}`, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(values)
            })
                .then(res => { 
                    if (!res.ok) {
                    throw new Error('failed to update product.')
                    }
                    return res.json()
            })
            .then(updatedProduct => console.log(updatedProduct))
            .catch(e => console.error(e))
        }
    })
    if (!product) {
        return <p>Loading...</p>
    }
    return (
        <div>
            
        </div>
    )



}

export default EditForm

