2018.03.19 M 11:00 
Capstone Proposal 
draft 1

#FIDDLEHEAD 
a performable web instrument

##Design Features: 
- a single page application with responsive design for desktop and mobile 
- Supports live interaction with sound, instant feedback with parameter changes
- Django server backend supporting user accounts to store songs and instrument presets

##Design Functionality:

A user will got to the fiddlehead homepage and immediately be greeted with the interactive panel and a default demo sequence.

Users can begin interacting immediately by pressing play and changing parameters, login not required.

If users want to save or recall previous work, they may login through the header link. This will display a dropdown menu to allow login access.

There are four sections to this application:
  1. Header. (top of page) A User login with dropdown in header, allows users to select songs and presets
  2. global transport (top middle) for play/stop/ff/rw functions, adding sequence building blocks
  3. sequencer (left side) for live interacting note attributes, pitch, velocity etc, while the sequence is running
  4. synthesizer (right side) for live interacting with timbral aspects of sound, such as frequency and envelope.  

##Components:
1. Transport. At the top of the view window, a timeline will display the current cursor position, scheduled sequences and transport buttons: play, stop, seek-next and seek-previous.
    1. When a user presses the play button, a global transport counter will begin updating with a delay based on the current beats per minute value.
The transport counter will continue incrementing, starting over after it reaches the end of the scheduled sequences, until a user presses the stop button.
    2. The seek buttons will set the counter to the beginning of the current sequence, previous sequence or beginning of the following sequence
2. Sound. The core functionality of this application is the html5 web audio component arrangement. It will consist of the following components.
    1. An oscillator node that will be updated and triggered every cycle of the main loop.
    2. A gain node that allows interaction with the amplification of the oscillator output, whether the sound eases in the way a wind instrument would or presents a sharp attack the way a piano might.
    3. An envelope node that allows interaction with the harmonic structure of the sound, whether the upper partials are dampened to mimic the deep sound of a bass instrument or unfiltered to produce shrill sounds.   
    4. A delay node that can produce delayed copies of the sound to facilitate rhythmic reflections to add temporal and stereo depth.
    5. A reverb node that produces reflections of the sound that imitate natural reverberations and lend the sound a spatial character.
    6. An oscilloscope node that will render a visual representation of the sound for the user
    7. A recorder node that allows the output sound to be captured and recorded.
    8. A master output node that will allow the sounds produced to be output to speakers.
3. Interactivity
    1. Sliders: when a user changes a slider value, vue will react immediately, updating component values. Each slider features an accompanying digital display that will update to show the change. The variable changes will change the properties of the component nodes, so the next iteration of the main loop will trigger different values.
    2. Digital displays. These are read only displays that are tied to each slider and display a numerical value for their parent slider.
    3. 'LEDs' these are simple elements that have an active that appears brighter, mimicking a lit LED and an inactive state, showing an unlit LED. These will be triggered when the sequence values correspond to their active cues.
    4. Drop down lists. These are selector pages that allow the user to select from a subset of hardcoded settings, such as the key and scale that notes will be bound to.
    5. Sequence Arrays displayed below the sequence sliders will feature a view button and an array showing the current sequence settings. 
        - Buttons. View toggle buttons for the sequencer section will switch which array of sequence components will be displayed. This will also hide the current sliders and display the sliders for the selected note attributes.
    6. Transport buttons will start/stop the current loop/change the counter values.
    7. Copy paste buttons in the transport menu will allow the user to arrange content into a song.
    6. Drop down header menu that allows the user to login and interact with saved songs and synth presets.
   
##Data Model:
User data will be stored in a sqlite3 database managed by django. It will consist of a few models:
1. Model: UserAccount. Stored with a name and id, linking to songs and presets. 
        One to many relationship as each user can have multiple songs and presets. 
2. Model: Song. Each song will have a name/id and consist of an ordered list of sequences.
3. Model: Sequence. Each sequence will have a name/id and chosen color and consist of several arrays of sequence attributes: notes, octave values, velocities, mutes, envelope amounts, note lengths, noise mix. 
4. Model: Preset. Synthesizer settings stored as presets linked with user accounts.

##Milestone Timeline
01. Hello Vue
02. Static page containers in vue.js
03. a play button triggering an oscillator note from a web Audio Component Node.
04. Reactive sliders with digital display.
05. Arrangement of sliders and buttons.
06. Slider templates, Variable sequence length changing the arrays and slider template displays.
07. Sequence buttons switch slider view.
08. change of sequence information affects playback.
09. Note deactivation.
10. Backend models to store users, songs, sequences, presets, 
11. Page refreshing front-back updating database when changes are presented/saved.
12. User accounts.
13. sequence visual representation in transport.
14. transport cut paste scheduling.
15. User security
16. Deployment onto AWS cloud server

