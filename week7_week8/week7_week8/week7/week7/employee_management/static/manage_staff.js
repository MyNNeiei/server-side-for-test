function addStaff(pro_id, csrf_token){
    const emp = document.getElementById('input-add-staff');
        const emp_id = emp.value;W
        
        // กำหนด path ให้ถูกต้อง
        fetch(`/project/${pro_id}/${emp_id}/add/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrf_token,
            }
        })
        .then(response => response.json())
        .then(data => { 
            console.log('Item updated successfully')
            window.location.reload()
        })
        .catch(error => console.error('Error:', error));
}


async function removeStaff(pro_id, emp_id, csrf_token){
    // กำหนด path ให้ถูกต้อง
    fetch(`/project/${pro_id}/${emp_id}/remove/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log('Item updated successfully')
        window.location.reload()
    })
    .catch(error => console.error('Error:', error));
}