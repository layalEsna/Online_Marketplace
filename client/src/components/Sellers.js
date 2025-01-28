import React, { useState, useEffect } from "react"
function Sellers() {
    const [sellers, setSellers] = useState([])

    useEffect(() => {
        fetch('http://127.0.0.1:5555/sellers')
            .then(res => {
                if (!res.ok) {
                    throw new Error('Failed to get sellers.')
                }
                return res.json()
            })
            .then(data => setSellers(data.sellers || []))
            .catch(e => console.error(`Internal error: ${e}`))
    }, [])

    return (
        <div>
            <ul>
                {sellers.map(seller =>
                    <li key={seller.id}>
                        <h3>{seller.username}</h3>
                        <ul>
                            {(seller.products || []).map(
                                product => (
                                    <li key={product.id}>
                                        <h4>{product.name}</h4>
                                        <img src={product.image} alt={product.name} style={{width:'100px'}}/>
                                        <p>{product.description}</p>
                                        <p>{product.price}</p>
                                        <button>buy</button>
                                    </li>
                                )
                            )}
                            
                        </ul>
                    </li>
                )}
            </ul>
        </div>
    )


}
export default Sellers
