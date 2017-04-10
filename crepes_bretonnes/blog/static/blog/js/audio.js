var lecteurApi = (function () {
    function Button(elementId, color) {
      this.element = document.getElementById(elementId);
      this.color = color;
      this.element.style.color = this.color;
    };


    function ButtonMulti(query) {
      this.elements = document.querySelectorAll(query);
    };

    function AudioReaderHtml(elementId) {
      this.element = document.getElementById(elementId)
    };

    function TextElement(elementId) {
      this.element = document.getElementById(elementId)
    };

    function addListenerMulti(element, eventNames, listener) {
      var events = eventNames.split(' ');
      for (var i=0, iLen=events.length; i<iLen; i++) {
        element.addEventListener(events[i], listener, false);
      }
    }

    var audioApi = {
      player: {
        objects: {},
        init: function () {
          this.objects = {
                                'audioReader': new AudioReaderHtml('audioReader'),
                                'startBtn':    new Button('start','blue'),
                                'pauseBtn':    new Button('pause','blue'),
                                'stopBtn':     new Button('stop','blue'),
                                'btnsVol':     new ButtonMulti('.btn-vol'),
                                'time':        new TextElement('progressTime'),
                          };

          var registeringEvent = (function (events) {
              for (var event in events) {
                events[event]();
              }
            })(audioApi.events);
        },
        start: function () {
            this.objects.audioReader.element.play();
        },
        pause: function () {
            this.objects.audioReader.element.pause();
        },
        stop: function () {
            this.objects.audioReader.element.currentTime = 0;
            this.objects.audioReader.element.pause();
        },
        changeVolume: function (value) {
          this.objects.audioReader.element.volume = value;
        },
        progressBar: function (e) {
          var duration = audioApi.player.objects.audioReader.element.duration;    // Durée totale
          var time     = audioApi.player.objects.audioReader.element.currentTime; // Temps écoulé
          var fraction = time / duration;
          var percent  = Math.ceil(fraction * 100);

          var progress = document.querySelector('#progressBar');

          progress.style.width = percent + '%';
          progress.textContent = percent + '%';
        },
        timeElapsed: function (e) {
          var time   = audioApi.player.objects.audioReader.element.currentTime; // Temps écoulé
          var hours  = Math.floor(time / 3600);
          var minute = Math.floor((time % 3600) / 60);
          var second = Math.floor((time % 3600) % 60);
          var secondText = ("0" + second.toString()).slice(-2);

          var progressTime = audioApi.player.objects.time.element;

          progressTime.innerHTML = minute + ':' + secondText;
        }
      },
      events: {
        play: function () {
          audioApi.player.objects.startBtn.element.addEventListener('click', function (e) {
            audioApi.player.start();
          });
        },
        pause: function () {
          audioApi.player.objects.pauseBtn.element.addEventListener('click', function (e) {
            audioApi.player.pause();
          });
        },
        stop: function () {
          audioApi.player.objects.stopBtn.element.addEventListener('click', function (e) {
            audioApi.player.stop();
          });
        },
        volume: function () {
            for (var i = 0, element; element = audioApi.player.objects.btnsVol.elements[i]; i++) {
                //work with element
              // alert('add volume');
              element.addEventListener('click', function (e) {
                audioApi.player.changeVolume(e.target.value);
              });
            }
        },
        timeUpdate: function() {
          audioApi.player.objects.audioReader.element.addEventListener('timeupdate', function () {
            audioApi.player.progressBar();
            audioApi.player.timeElapsed();
          });
        },
      } // End of event
    }

    var run = function () {
      audioApi.player.init();
    }();

    console.log(audioApi.event)

    return audioApi;
})();
