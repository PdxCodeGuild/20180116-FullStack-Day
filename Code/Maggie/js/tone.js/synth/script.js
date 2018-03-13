window.onload = function () {
  

  //html selectors

  //SEQUENCER

  let scale_ddl = document.querySelector('#scale_ddl');
  let s_len_sl = document.querySelector('#s_len_sl');
  let s_rng_sl = document.querySelector('#s_rng_sl');
  

  // buttons
  let play_bt = document.querySelector('#play_bt');
  let stop_bt = document.querySelector('#stop_bt');

  // let s_port_sl = document.querySelector('#s_port_sl');

  //SYNTH
  let wav_ddl = document.querySelector('#wav_ddl');
  let s_bpm_sl = document.querySelector('#s_bpm_sl');
  let s_oct_sl = document.querySelector('#s_oct_sl');

  // let n_len_ddl = document.querySelector('#n_len_ddl');


  //amp
  let a_atk_sl = document.querySelector('#a_atk_sl');
  let a_sus_sl = document.querySelector('#a_sus_sl');
  let a_dec_sl = document.querySelector('#a_dec_sl');
  let a_rel_sl = document.querySelector('#a_rel_sl');
  //filter
  let f_atk_sl = document.querySelector('#f_atk_sl');
  let f_sus_sl = document.querySelector('#f_sus_sl');
  let f_dec_sl = document.querySelector('#f_dec_sl');
  let f_rel_sl = document.querySelector('#f_rel_sl');
  let f_frq_sl = document.querySelector('#f_frq_sl');
  let f_env_sl = document.querySelector('#f_env_sl');
  let f_q_sl = document.querySelector('#f_q_sl');
  let f_gain_sl = document.querySelector('#f_gain_sl');

  let d_time_sl = document.querySelector('#d_time_sl');
  let d_fdbk_sl = document.querySelector('#d_fdbk_sl');
  let d_wet_sl = document.querySelector('#d_wet_sl');

  let r_rm_s_sl = document.querySelector('#r_rm_s_sl');
  let r_wet_sl = document.querySelector('#r_wet_sl');

  //VARIABLES
  let stop = false;
  let note_array = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'];//test array




  //INST OBJECTS & init values
  let reverb = new Tone.Freeverb({
    "roomSize" : 0.5,
    "dampening" : 3000
  }).toMaster();
  
   let delay = new Tone.PingPongDelay({
      "delayTime"  : 0.01,
      "wet" : 0.1,
      "feedback" : 0.1
  }).connect(reverb);
  
  let synth = new Tone.MonoSynth().connect(delay);
    //construct a sequence





  //PLAY button click
  play_bt.onclick = function() {
    clearTimeout();  
    // let note_length = n_len_ddl.options[n_len_ddl.selectedIndex].value;
    //ms delay converted to bpm
    let retrigger_delay = parseInt(60000/(s_bpm_sl.value));
    //reset stop to off for conditional  
    stop = false;
    //random starting note from array
    let starting_note = `${note_array[Math.floor(Math.random() * (note_array.length - 1))]}3`; //hardcoded to 3oct currently
    //the range of notes in scale
    let note_range = parseInt(s_rng_sl.value);
    // console.log(note_range);
    let scale_name = scale_ddl.options[scale_ddl.selectedIndex].value;
    let sequence_length = s_len_sl.value;
    // create the array of note frequencies
  let note_freqs = ScaleMaker.makeScale(scale_name, starting_note, note_range).inHertz;
    // console.log(note_freqs);



  function new_sequence(length) {
    //empty seq to be filled
    let sequence = [];
    //grab random notes for sequence
    for (let i = 0; i < length; i++) {
      let random_note_index = Math.floor(Math.random() * note_range);
      let random_note = note_freqs[random_note_index];
      sequence.push(random_note);
    }
    return sequence;
  }




    let sequence_1 = new_sequence(sequence_length);
    //setting initial values
    let cursor_position = 0;
    let sequence_position = 0;
    //update interval  
    let interval = setTimeout(function(){update_values() }, retrigger_delay);
    function update_values() {
      clearTimeout();
      //updating bpm
      retrigger_delay = parseInt(60000/(s_bpm_sl.value));
      //drop down osc
      synth.oscillator.type = wav_ddl.options[wav_ddl.selectedIndex].value;
      // synth.portamento = s_port_sl.value;
      // delay.delayTime.value = (s_bpm_sl.value) * Math.pow(2,s_oct_sl.value);
      
      //measure delay by the overall delay rate
      delay.delayTime.value = (retrigger_delay/1000) * d_time_sl.value;
      
      delay.feedback.value = d_fdbk_sl.value;
      // console.log(delay.feedback.value);
      delay.wet.value = d_wet_sl.value;
      
      reverb.roomSize.value = r_rm_s_sl.value,
      reverb.wet.value = r_wet_sl.value;
      
      synth.envelope.attack = a_atk_sl.value;
      synth.envelope.decay = a_dec_sl.value;
      synth.envelope.sustain = a_sus_sl.value;
      synth.envelope.release = a_rel_sl.value;
      
      synth.filterEnvelope.attack = f_atk_sl.value;
      synth.filterEnvelope.decay = f_dec_sl.value;
      synth.filterEnvelope.sustain = f_sus_sl.value;
      synth.filterEnvelope.release = f_rel_sl.value;
      synth.filterEnvelope.baseFrequency = f_frq_sl.value; 
      synth.filterEnvelope.octaves = f_env_sl.value;   
      // synth.filter.Q = f_q_sl.value;
      synth.filterEnvelope.exponent = f_gain_sl.value;

      console.log(synth.filter.Q);
        //SYNTH trigger note on interval
       // octave shift value is multiplying freq by pow of 2   
      synth.triggerAttackRelease((sequence_1[sequence_position] * Math.pow(2,s_oct_sl.value)), '2n');
      cursor_position += 1;
     
      //sequence repeats after reaching end
      sequence_position =  cursor_position  % sequence_1.length;
      //stop if stop button
      if (stop === true) {
        clearTimeout(interval);  
        return;
      } 
      setTimeout(function(){update_values()}, retrigger_delay)
    }
  }                             
    //STOP!
  stop_bt.onclick = function() {
    stop = true;
    return stop;
  } 
}                           
