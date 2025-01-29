

// import React from "react";
// import { useFormik } from 'formik'
// import { useNavigate, useParams } from "react-router-dom";
// import * as Yup from 'yup'

// function EditForm() {

//     const { username, productId } = useParams()
//     const navigate = useNavigate()
import React, { useEffect, useState } from "react";
import { useFormik } from 'formik'
import { useParams, useNavigate} from "react-router-dom";
import * as Yup from 'yup'

function EditForm() {

    const { username, productId } = useParams()
    const [product, setProduct] = useState(null)
    const navigate = useNavigate()

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
            // fetch(`http://127.0.0.1:5555/sellers/${username}/`, {
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
            <form onSubmit={formik.handleSubmit}>
                <label htmlFor="name">Product Name</label>
                <input

                    id="name"
                    name="name"
                    type="text"
                    value={formik.values.name}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}   
                    
                />
                {formik.errors.name && formik.touched.name && (
                        <div>{ formik.errors.name }</div>
                )}
                <label htmlFor="image">Image URL</label>
                <input

                    id="image"
                    name="image"
                    type="text"
                    value={formik.values.image}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}   
                    
                />
                {formik.errors.image && formik.touched.image && (
                        <div>{ formik.errors.image }</div>
                )}
                <label htmlFor="description">DescriptionL</label>
                <input

                    id="description"
                    name="description"
                    type="text"
                    value={formik.values.description}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}   
                    
                />
                {formik.errors.description && formik.touched.description && (
                        <div>{ formik.errors.description }</div>
                )}
                <label htmlFor="price">Price</label>
                <input

                    id="price"
                    name="price"
                    type="number"
                    value={formik.values.price}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}   
                    
                />
                {formik.errors.price && formik.touched.price && (
                        <div>{ formik.errors.price }</div>
                )}

                <button type="submit">submit</button>
            </form>

        </div>
    )



}

export default EditForm

