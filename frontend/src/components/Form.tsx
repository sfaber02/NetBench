import React, { ChangeEvent } from 'react';



/* Input fields

Title, X-Axis Label, Width, Height, Line color, Theme, Tags, 
Host, Port, Interval, Test Length 

*/

type TextInputProps = {
  value: string;
  onChange: (event: ChangeEvent<HTMLInputElement>) => void;
  placeholder?: string;
  label?: string;
};

const Form: React.FC<TextInputProps> = ({ value, onChange, placeholder = '', label }) => {
  return (
    <div>
      {label && <label>{label}</label>}
      <input
        type="text"
        value={value}
        onChange={onChange}
        placeholder={placeholder}
      />
    </div>
  );
};

export default Form;



























