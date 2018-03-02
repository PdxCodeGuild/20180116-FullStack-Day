



document.getElementById("clicked").onclick = function () {

    let recs = [
    'https://www.discogs.com/Various-Blue-Skied-An-Clear-A-Morr-Music-Compilation/master/60921',
    'https://www.discogs.com/Vikki-Jackman-Of-Beauty-Reminiscing/master/42075',
    'https://www.discogs.com/Gary-Numan-The-Pleasure-Principle/master/70133',
    'https://www.discogs.com/Section-25-Always-Now/master/55226',
    'https://www.discogs.com/COH-Above-Air/master/960452',
    'https://www.discogs.com/Cindytalk-A-Life-Is-Everywhere/master/558435',
    'https://www.discogs.com/Antlers-Mulm-The-Age-Of-Efficiency/master/337539',
    'https://www.discogs.com/Current-93-Thunder-Perfect-Mind/master/22268',
    'https://www.discogs.com/Alva-Noto-Xerrox-Vol2/master/173456',
    'https://www.discogs.com/Byetone-Symeta/master/391269',
    'https://www.discogs.com/Godspeed-You-Black-Emperor-Luciferian-Towers/master/1240374',
    'https://www.discogs.com/Sonic-Youth-Bad-Moon-Rising/master/9808',
    'https://www.discogs.com/Autechre-Confield/master/1374',
    'https://www.discogs.com/Coil-The-Ape-Of-Naples/master/5642',
    'https://www.discogs.com/Coil-Presents-Black-Light-District-A-Thousand-Lights-In-A-Darkened-Room/master/6807',
    'https://www.discogs.com/DRI-Dealing-With-It/master/16443',
    'https://www.discogs.com/Angels-Of-Light-We-Are-Him/master/8511',
    'https://www.discogs.com/Godspeed-You-Black-Emperor-Lift-Your-Skinny-Fists-Like-Antennas-To-Heaven/release/74260?ev=rr',
    'https://www.discogs.com/Nick-Cave-The-Bad-Seeds-Push-The-Sky-Away/master/519359',
    'https://www.discogs.com/These-Immortal-Souls-Im-Never-Gonna-Die-Again-/master/213907',
    'https://www.discogs.com/Black-Marble-Its-Immaterial/master/1071230',
    'https://www.discogs.com/Brendan-Walls-Andrew-Chalk-This-Growing-Clearing/release/582278',
    'https://www.discogs.com/The-Misfits-Static-Age/master/105468',
    'https://www.discogs.com/Aglaia-Mondi-Sensibili/release/803661',
    'https://www.discogs.com/Rowland-S-Howard-Pop-Crimes/master/216098',
    'https://www.discogs.com/Cylob-Cylobian-Sunset/release/82128',
    'https://www.discogs.com/Various-MASK-500/master/203080',
    'https://www.discogs.com/Autechre-Gescom-Keynell-Keynell/master/134096',
    'https://www.discogs.com/Suicidal-Tendencies-Suicidal-Tendencies/master/18713',
    'https://www.discogs.com/Cyclobe-Wounded-Galaxies-Tap-At-The-Window/master/289307',
    'https://www.discogs.com/Christian-Death-Only-Theatre-Of-Pain/master/2053',
    'https://www.discogs.com/Black-Flag-The-First-Four-Years/master/28709',
    ];

    let picked = Math.floor(Math.random() * recs.length);
    location.href = recs[picked];

    };