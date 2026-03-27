import TextType from './component/TextType';
import './App.css';
import CardNav from './component/CardNav';
import FloatingLines from './component/FloatingLines';
import TrueFocus from './component/TrueFocus';


import logo from './logo.svg';

const items = [
  {
    label: 'About',
    bgColor: '#0D0716',
    textColor: '#fff',
    links: [
      { label: 'Company', ariaLabel: 'About Company' },
      { label: 'Careers', ariaLabel: 'About Careers' }
    ]
  },
  {
    label: 'Projects',
    bgColor: '#170D27',
    textColor: '#fff',
    links: [
      { label: 'Featured', ariaLabel: 'Featured Projects' },
      { label: 'Case Studies', ariaLabel: 'Project Case Studies' }
    ]
  },
  {
    label: 'Contact',
    bgColor: '#271E37',
    textColor: '#fff',
    links: [
      { label: 'Email', ariaLabel: 'Email us' },
      { label: 'Twitter', ariaLabel: 'Twitter' },
      { label: 'LinkedIn', ariaLabel: 'LinkedIn' }
    ]
  }
];

function App() {
  return (
<>

      <CardNav
        logo={logo}
        logoAlt="Company Logo"
        items={items}
        baseColor="#fff"
        menuColor="#000"
        buttonBgColor="#111"
        buttonTextColor="#fff"
        ease="power3.out"
        theme="light"
      />
    
<div className="hero-section">
  <div className="hero-lines">
    <FloatingLines 
      enabledWaves={["top","middle","bottom"]}
      // Array - specify line count per wave; Number - same count for all waves
      lineCount={5}
      // Array - specify line distance per wave; Number - same distance for all waves
      lineDistance={5}
      bendRadius={5}
      bendStrength={-0.5}
      interactive={true}
      parallax={true}
    />
  </div>

   <CardNav
        logo={logo}
        logoAlt="Company Logo"
        items={items}
        baseColor="#fff"
        menuColor="#000"
        buttonBgColor="#111"
        buttonTextColor="#fff"
        ease="power3.out"
        theme="light"
      />

  <div className="hero-text">
    

<TrueFocus 
sentence="True Focus"
manualMode={false}
blurAmount={5}
borderColor="#5227FF"
animationDuration={0.5}
pauseBetweenAnimations={1}
/>



<TextType 
  text={["Text typing effect", "for your websites", "Happy coding!"]}
  typingSpeed={75}
  pauseDuration={1500}
  showCursor
  cursorCharacter="_"
  texts={["Welcome to React Bits! Good to see you!","Build some amazing experiences!"]}
  deletingSpeed={50}
  variableSpeedEnabled={false}
  variableSpeedMin={60}
  variableSpeedMax={120}
  cursorBlinkDuration={0.5}
/>

  </div>
</div>



</>
  );
}

export default App;
