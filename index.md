
<div class="container">
    <div class="row">
        <div class="video-container">
            <iframe width="560" height="200" src="https://www.youtube.com/embed/x7SQaDTSrVg?si=P9QG5xO2NpJu3lrt?&autoplay=1&mute=1&playsinline=1&controls=0&showinfo=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        </div>
        <div class="col-sm-4">
            <form class="form-auth" action="/login/includes/login.inc.php" method="post">
                <?php insert_csrf_token(); ?>
                <div class="text-center">
                    <img width="200" height="200" src="https://cdn.discordapp.com/attachments/909947635715153952/1159715288594518016/image-removebg-preview.png?ex=65320807&is=651f9307&hm=7e5c7faa637bf72b94c41a70a23ca13ab65531bd9cb90d7604379ac76f6560b1&">
                </div>
                <h6>Welcome back to Whisp</h6>
                <div class="text-center mb-3">
                    <small class="text-success font-weight-bold">
                        <?php
                            if (isset($_SESSION['STATUS']['loginstatus']))
                                echo $_SESSION['STATUS']['loginstatus'];
                        ?>
                    </small>
                </div>
                <div class="form-group">
                    <label for="username" class="sr-only">Username</label>
                    <input type="text" id="username" name="username" class="form-control" placeholder="Username" required autofocus>
                    <sub class="text-danger">
                        <?php
                            if (isset($_SESSION['ERRORS']['nouser']))
                                echo $_SESSION['ERRORS']['nouser'];
                        ?>
                    </sub>
                </div>
                <div class="form-group">
                    <label for="password" class="sr-only">Password</label>
                    <input type="password" id="password" name="password" class="form-control" placeholder="Password" required>
                    <sub class="text-danger">
                        <?php
                            if (isset($_SESSION['ERRORS']['wrongpassword']))
                                echo $_SESSION['ERRORS']['wrongpassword'];
                        ?>
                    </sub>
                </div>
                <div class="col-auto my-1 mb-4">
                    <div class="custom-control custom-checkbox mr-sm-2">
                        <input type="checkbox" class="custom-control-input" id="rememberme" name="rememberme">
                        <label class="custom-control-label" for="rememberme">Remember me</label>
                    </div>
                </div>
                <button class="btn btn-lg btn-primary btn-block" type="submit" value="loginsubmit" name="loginsubmit">Login</button>
                <a class="nav-link text-center" href="../register/">Signup</a>
                <p class="mt-4 mb-3 text-muted text-center">
                    </a>
                </p>
            </form>
        </div>
        <div class="col-sm-4">
        </div>
    </div>
</div>
<style>
html,
body {
    overflow: hidden;
    height: 100%;
    background-color: #36393F;
    color: #FFF;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
h6 {
    color: white;
    text-align: center;
}
.box-shadow {
    box-shadow: 0 .25rem .75rem rgba(0, 0, 0, .05);
}
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
.form-auth {
    background-color: #202225;
    position: absolute;
    color: #FFFFFF;
    left: 97%;
    /* transform: translate(0%, -135%); */
}
.form-auth .checkbox {
    font-weight: 400;
    color: #FFF;
}
.form-auth .form-control {
    box-sizing: border-box;
    height: auto;
    padding: 10px;
    font-size: 16px;
    color: white;
    background-color: #36393F;
}
.form-auth .form-control:focus {
    z-index: 2;
    border-color: #7289DA;
}
.form-auth input[type="email"],
.form-auth input[type="password"] {
    color: #FFFFFF;
    background-color: #36393F;
    border: none;
}
.video-container{
        pointer-events: none;
        width: 100vw;
        height: 100vh;
    }
    iframe {
        pointer-events: none;
        position: absolute;
        top: 50%;
        left: 50%;
        width: 125vw;
        height: 150vh;
        transform: translate(-50%, -47%);
    }
</style>