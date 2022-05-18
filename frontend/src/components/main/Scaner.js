
import React , {useState} from 'react'
import { QrReader } from 'react-qr-reader';
import ReslutModal from './ReslutModal';

const Scaner = () => {
    const [data, setData] = useState('No result');
    const [Modal,setModal]=useState(false)
    return (
      <>
      
        <QrReader
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
          style={{ width: '100%' }}
        />
        <p>{data}</p>
        {
            Modal?<ReslutModal props={data}/>:<></>
        }
      </>
    );
}

export default Scaner