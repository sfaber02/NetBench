async function communicateWithPython(message: string) {
    try {
        const response = await fetch('http://localhost:8000/api/test', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message }),
        });
        return await response.json();
    } catch (error) {
        throw new Error('Error communicating with backend');
    }
}

// async function startTest() {
//     try:
//
// }
export { communicateWithPython };
