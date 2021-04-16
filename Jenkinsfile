pipeline {
    agent {
        label 'deb'
    }


    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                sh "cd /srv; rm -rf net-gargoyle2"
                sh "rm -rf net-gargoyle2; git clone https://github.com/jpegleg/net-gargoyle2"
                sh "chmod +x install"
                sh "rm -rf /usr/local/sbin/net-gargoyle /usr/local/sbin/reportIps /opt/net-gargoyle/workspace/*"
                sh "./install"
            }
            post {
                success {
                    sh "ls /usr/local/sbin/net-gargoyle"
                    sh "ls /usr/local/sbin/reportIps"
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
                sh "pip3 install bandit"
                sh "pip3 install psutil"
                sh "cd /opt/net-gargoyle/workspace"
                sh "bandit --exit-zero -r . > /srv/net-gargoyle_bandit-report.txt"
                sh "rm /opt/net-gargoyle/workspace/gargoyle.db 2>/dev/null"
                sh "python3 net_set.py || exit 1"
                sh "python3 net_check.py || exit 1"
                // popnet is the same as kill-netg but in the /usr/local/bin for the jenkins build agent
                sh "/usr/local/bin/popnet"
                sh "/usr/local/sbin/net-gargoyle || exit 1"
            }
            post {
                success {
                    sh "pgrep -f 'python3 net_mon.py'"
                }
            }
        }
        stage('Publish') {
            steps {
                // make a tarball for pick up
                sh "tar czvf /srv/net-gargoyle2_build.tgz /srv/workspace/jpegleg-repo_net-gargoyle2_main/ && touch /srv/net-gargoyle2_pickup.lock"              
                sh "mkdir -p /srv/debbuild/net-gargoyle2-1.0.0/DEBIAN/; mkdir -p /srv/debbuild/net-gargoyle2-1.0.0/usr/local/sbin/; mkdir -p /srv/debbuild/net-gargoyle2-1.0.0/opt/net-gargoyle/workspace/BUILD >/dev/null"
                sh "cp /srv/workspace/jpegleg-repo_net-gargoyle2_main/net-gargoyle2.control /srv/debbuild/net-gargoyle2-1.0.0/DEBIAN/control"
                sh "cp /srv/workspace/jpegleg-repo_net-gargoyle2_main/postinst /srv/debbuild/net-gargoyle2-1.0.0/DEBIAN/postinst"
                sh "chmod +x /srv/debbuild/net-gargoyle2-1.0.0/DEBIAN/postinst"
                sh "cp /srv/workspace/jpegleg-repo_net-gargoyle2_main/net-gargoyle /srv/debbuild/net-gargoyle2-1.0.0/usr/local/sbin/net-gargoyle"
                sh "cp /srv/workspace/jpegleg-repo_net-gargoyle2_main/reportIps /srv/debbuild/net-gargoyle2-1.0.0/usr/local/sbin/reportIps"
                sh "cp /srv/workspace/jpegleg-repo_net-gargoyle2_main/kill-netg /srv/debbuild/net-gargoyle2-1.0.0/usr/local/sbin/"
                sh "chmod +x /srv/debbuild/net-gargoyle2-1.0.0/usr/local/sbin/*"
                sh "cp -r /srv/workspace/jpegleg-repo_net-gargoyle2_main/* /srv/debbuild/net-gargoyle2-1.0.0/opt/net-gargoyle/workspace/BUILD/"
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
                    sh "ls -larth /usr/local/sbin/net-gargoyle || exit 1"
                    sh "echo net-gargoyle2 > /srv/net-g.sums.txt"
                    sh "sha256sum /srv/net-gargoyle2-1.0.0.deb >> /srv/net-g.sums.txt"
                    sh "sha1sum /srv/net-gargoyle2-1.0.0.deb >> /srv/net-g.sums.txt"
                    sh "md5sum /srv/net-gargoyle2-1.0.0.deb >> /srv/net-g.sums.txt"
                }
            }
        }
    }
}
