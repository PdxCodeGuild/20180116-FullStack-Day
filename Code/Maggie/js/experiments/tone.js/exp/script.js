//html selectors
let play_bt = document.querySelector('#play_bt');
let stop_bt = document.querySelector('#stop_bt');
//amp
let a_atk_sl = document.querySelector('#a_atk_sl');
let a_sus_sl = document.querySelector('#a_sus_sl');
let a_dec_sl = document.querySelector('#a_dec_sl');
let a_rel_sl = document.querySelector('#a_rel_sl');
//filter
let f_atk_sl = document.querySelector('#f_atk_sl');

let f_freq = 400;
let f_atk = 0.5;
let f_dec = 0.8;
let f_sus = 0.2;
let f_rel = 1.0;

//global vars
// let synth = new Tone.MonoSynth({
//      "portamento" : 0.01,
//      "oscillator" : {
//        "type" : "sawtooth"
//      },
//      "envelope" : {
//        "attack" : a_atk_sl.value,
//        "decay" : a_dec_sl.value,
//        "sustain" : a_sus_sl.value,
//        "release" : a_rel_sl.value,
//      },
//      "filterEnvelope" : {
//        "attack" : f_atk,
//        "decay" : f_dec,
//        "sustain" : f_sus,
//        "release" : f_rel,
//        "baseFrequency" : f_freq,
//        "octaves" : 2,
//         "rolloff" : -12
//      }
//    }).toMaster();
//master variables
let note_array = ['A3','B3','C3','D3','E3','F3','G3'];
let sequence_length = 24;
// let note_position = 0;
let end_position = sequence_length * 8;

let retrigger_delay = 500;
let scale_name = 'chinesePentatonic';
let starting_note = note_array[Math.floor(Math.random() * note_array.length)];
// let starting_note = 'C3';

let note_range = 10;
let measure_lengths = ['1m', '2m', '4m', '8m', '16m', '32m'];
let note_lengths = ['4n', '8n', '16n'];
let note_length = note_lengths[2];

// create the array of note frequencies
let note_freqs = ScaleMaker.makeScale(scale_name, starting_note, note_range).inHertz;
function new_sequence(length) {
  let sequence = [];
  for (let i = 0; i < length; i++) {
    let random_note_index = Math.floor(Math.random() * note_range);
    let random_note = note_freqs[random_note_index];
    sequence.push(random_note);
  }
  return sequence;
}
let sequence_1 = new_sequence(sequence_length);
// let sequence_2= new_sequence(sequence_length);
//on interval start, value will be chosen from notes at note position

let stop = false;
//button click
play_bt.onclick = function() {
  stop = false;
  let cursor_position = 0;
  let sequence_position = 0;
  let interval = setInterval(function(){
    
  //setup synth
let synth = new Tone.MonoSynth({
      "portamento" : 0.01,
      "oscillator" : {
        "type" : "sawtooth"
      },
      "envelope" : {
        "attack" : a_atk_sl.value,
        "decay" : a_dec_sl.value,
        "sustain" : a_sus_sl.value,
        "release" : a_rel_sl.value,
      },
      "filterEnvelope" : {
        "attack" : f_atk,
        "decay" : f_dec,
        "sustain" : f_sus,
        "release" : f_rel,
        "baseFrequency" : f_freq,
        "octaves" : 2,
        "rolloff" : -12
      }
    }).toMaster(); 
    
    
    
    //SYNTH <3 trigger note on interval
  synth.triggerAttackRelease(sequence_1[sequence_position], note_length);
    cursor_position += 1;
   
    //updates
    // a_atk_span.innerText = a_atk;
    
    let measure = cursor_position/4
    // console.log(measure);
    // f_atk = cursor_position % 4;
    // f_freq = cursor_position % 2000;
    
    //for repeating notes
    sequence_position =  cursor_position  % sequence_1.length;
    if (stop === true) {
      clearInterval(interval);  
    } 
    if (cursor_position >= end_position) {
      clearInterval(interval);
    }
  }, retrigger_delay);
}

stop_bt.onclick = function() {
  stop = true;
  return stop;
} 
//interval is currently increasing.
//clearing at the end of its length
//I'd like to arrange 
//when to clear interval... lets make it reference a global