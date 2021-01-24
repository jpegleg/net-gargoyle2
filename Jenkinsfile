pipeline {
    agent {
        label 'deb'
    }


    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                sh "cd /srv; rm -rf net-gargoyle2"
                git 'https://github.com/jpegleg/net-gargoyle2'
                sh "chmod +x install"
                sh "rm -f /usr/local/bin/net-gargoyle /usr/local/bin/reportIps /opt/net-gargoyle/workspace/*"
                sh "./install"
            }
            post {
                success {
                    sh "ls /usr/local/bin/net-gargoyle"
                    sh "ls /usr/local/bin/reportIps"
                    sh "ls /opt/net-gargoyle/workspace/net_gargoyle.py"
                    sh "ls /opt/net-gargoyle/workspace/net_mon.py"
                    sh "ls /opt/net-gargoyle/workspace/net_check.py"
                    sh "ls /opt/net-gargoyle/workspace/net_set.py"
                }
            }
        }
        stage('Tests') {
            steps {
                // test the program
                sh "source /opt/net-gargoyle/workspace/ngrvenv/bin/activate"
                sh "pip3 install bandit"
                sh "cd /opt/net-gargoyle/workspace"
                sh "bandit ."
            }
            post {
                success {
                    sh "net-gargoyle "
                }
            }
        }
        stage('Publish') {
            steps {
                // make a tarball for pick up
                sh "tar czvf /srv/net-gargoyle2_build.tgz /srv/net-gargoyle2 && touch /srv/net-gargoyle2_pickup.lock"
                
                sh "mkdir -p /srv/debbuild/net-gargoyle2-1.0.0/DEBIAN/; mkdir -p /srv/debbuild/net-gargoyle2-1.0.0/usr/local/bin/; mkdir -p /srv/debbuild/net-gargoyle2-1.0.0/opt/net-gargoyle/workspace/ >/dev/null"
                sh "cp /srv/workspace/net-gargoyle2.control /srv/debbuild/net-gargoyle2-1.0.0/DEBIAN/control"
                sh "cp /srv/workspace/net-gargoyle2/postinst /srv/debbuild/net-gargoyle2-1.0.0/DEBIAN/postinst"
                sh "chmod +x /srv/debbuild/h2b2-2.0.0/DEBIAN/postinst"
                sh "cp /usr/local/bin/net-gargoyle /srv/debbuild/h2b2-2.0.0/usr/local/bin/net-gargoyle"
                sh "cp /usr/local/bin/reportIps /srv/debbuild/h2b2-2.0.0/usr/local/bin/reportIps"
                sh "cp /opt/net-gargoyle/workspace/*.py /srv/debbuild/h2b2-2.0.0/opt/net-gargoyle/workspace/"
                sh "cd /srv/debbuild/ && tar czvf net-gargoyle2-1.0.0.tar.gz net-gargoyle2-1.0.0/ && dpkg -b ./net-gargoyle2-1.0.0 ./net-gargoyle2-1.0.0.deb"
            }
            post {
                success {
                    sh "ls /srv/net-gargoyle2_build.tgz || exit 1"
                    sh "cp /srv/debbuild/*.deb /srv/ && touch /srv/net-gargoyle2_pickup.lock"
                }
            }
        }
        stage('deb Tests') {
            steps {
                // test the deb
                sh "bash /srv/debuild net-gargoyle2-1.0.0.deb"
            }
            post {
                success {
                    sh "ls -larth /usr/local/bin/net-gargoyle || exit 1"
                }
            }
        }
    }
}
