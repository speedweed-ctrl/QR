
import React , {useState} from 'react'
import { QrReader } from 'react-qr-reader';
import ReslutModal from './ReslutModal';
import './a.css'
const Scaner = () => {
    const [data, setData] = useState('No result');
    const [Modal,setModal]=useState(false)
    const res=data.split('.')
    
    return (
      <>
      <div class="grid place-items-center h-screen">
        <div id="content">
      <QrReader
        className=' w-screen h-4/6 '
          onResult={(result, error) => {
            if (!!result) {
              setData(result.text);
              setModal(true)
              
              
            }
  
            if (!!error) {
              console.info(error);
            }
          }}
          constraints={{ facingMode: 'environment' }}
          
        />
        </div>
</div>
        
        {
            Modal?<ReslutModal props={res}/>:<></>
        }
      </>
    );
}

export default Scaner
