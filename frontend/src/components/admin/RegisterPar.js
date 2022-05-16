import axios from 'axios'
import React , {useState} from 'react'


const RegisterPar = () => {
    const [cin,setcin]=useState('')
    const[name,setname]=useState('')
    const[last,setlast]=useState('')
    const[mail,setmail]=useState('')
    const config = {
        headers: { Authorization: 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUzMzQ0NDM0LCJpYXQiOjE2NTI3Mzk2MzQsImp0aSI6IjJkN2U2MDhmM2U4MDQxYjhiYmVhZmE3MzkwOGE0ZTcxIiwidXNlcl9pZCI6M30.pSbUb9K4evOK6_DC5S4w9FRMYZBzbwnGVXBYm8wto0o'}
    };
    const submiHandler =async (e)=>{
        e.preventDefault()
       const {data} = await axios.post('http://192.168.1.11:8000/api/participant',{
            name:name,
            last_name:last,
            email:mail,
            cin:cin,
            
            
        },config)
        console.log(data)

    }
  return (
    <div className="lg:flex">
                <div className="lg:w-1/2 xl:max-w-screen-sm">
                    
                    <div className="mt-10 px-12 sm:px-24 md:px-48 lg:px-12 lg:mt-16 xl:px-24 xl:max-w-2xl">
                        <h2 className="text-center font-Avalon  text-4xl text-cl font-display font-semibold lg:text-left xl:text-5xl
                        xl:text-bold">register Participant</h2>
                        <div className="mt-12">
                            <form onSubmit={(e)=>(submiHandler(e))}>
                                <div>
                                    <div className="text-sm font-bold text-gray-700 tracking-wide">first name</div>
                                    <input className="w-full text-lg py-2 border-b border-gray-300 focus:outline-none focus:border-indigo-500" type="text" required placeholder="participant first name" value={name} onChange={(e)=>(setname(e.target.value))}/>
                                </div><br/>
                                <div>
                                    <div className="text-sm font-bold text-gray-700 tracking-wide">last name</div>
                                    <input className="w-full text-lg py-2 border-b border-gray-300 focus:outline-none focus:border-indigo-500" type="text" required placeholder="participant last name" value={last} onChange={(e)=>(setlast(e.target.value))}/>
                                </div><br/>
                                <div>
                                    <div className="text-sm font-bold text-gray-700 tracking-wide">cin</div>
                                    <input className="w-full text-lg py-2 border-b border-gray-300 focus:outline-none focus:border-indigo-500" type="text" required placeholder="cin" value={cin} onChange={(e)=>(setcin(e.target.value))}/>
                                </div><br/>
                                <div>
                                    <div className="text-sm font-bold text-gray-700 tracking-wide">email</div>
                                    <input className="w-full text-lg py-2 border-b border-gray-300 focus:outline-none focus:border-indigo-500" type='email' required placeholder="participant email adress"value={mail} onChange={(e)=>(setmail(e.target.value))}/>
                                </div>
                                
                                
                                <div className="mt-10">
                                    <button className="bg-cl font-Avalon text-gray-100 p-4 mb-3 w-full rounded-full tracking-wide
                                    font-semibold font-display focus:outline-none focus:shadow-outline hover:bg-indigo-600
                                    shadow-lg" type='submit'>
                                        Register Participant
                                    </button><br/>
                                </div>
                            </form>
                            
                        </div>
                    </div>
                </div>
                <div className="hidden lg:flex items-center justify-center bg-indigo-100 flex-1 h-screen">
                    <div className="max-w-xs transform duration-200 hover:scale-110 cursor-pointer">
                       
                    </div>
                </div>
            </div>
  )
}

export default RegisterPar