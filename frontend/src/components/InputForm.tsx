import React, { ChangeEvent, useState } from 'react';

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

const InputForm: React.FC<TextInputProps> = ({ value, onChange, placeholder = '', label }) => {
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

const FormContainer: React.FC = () => {
  const [formValues, setFormValues] = useState({
    title: '',
    xAxisLabel: '',
    width: '',
    height: '',
    lineColor: '',
    theme: '',
    tags: '',
    host: '',
    port: '',
    interval: '',
    testLength: '',
  });

  const handleChange = (field: string) => (event: ChangeEvent<HTMLInputElement>) => {
    setFormValues({
      ...formValues,
      [field]: event.target.value
    });
  };

  return (
    <form>
      <InputForm label="Title" value={formValues.title} onChange={handleChange('title')} />
      <InputForm label="X-Axis Label" value={formValues.xAxisLabel} onChange={handleChange('xAxisLabel')} />
      <InputForm label="Width" value={formValues.width} onChange={handleChange('width')} />
      <InputForm label="Height" value={formValues.height} onChange={handleChange('height')} />
      <InputForm label="Line Color" value={formValues.lineColor} onChange={handleChange('lineColor')} />
      <InputForm label="Theme" value={formValues.theme} onChange={handleChange('theme')} />
      <InputForm label="Tags" value={formValues.tags} onChange={handleChange('tags')} />
      <InputForm label="Host" value={formValues.host} onChange={handleChange('host')} />
      <InputForm label="Port" value={formValues.port} onChange={handleChange('port')} />
      <InputForm label="Interval" value={formValues.interval} onChange={handleChange('interval')} />
      <InputForm label="Test Length" value={formValues.testLength} onChange={handleChange('testLength')} />
    </form>
  )


}
export default FormContainer;



























