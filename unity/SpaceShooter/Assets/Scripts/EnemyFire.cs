using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyFire : MonoBehaviour
{
    [SerializeField]
    private int speed = -200;
    [SerializeField]
    private float rate = 0.5f;
    [SerializeField]
    private GameObject laserPrefab;
    private float time = 1.0f;

    void Start()
    {
        InvokeRepeating("Shoot", time, rate);
    }
    void Update()
    {
        
    }

    void Shoot()
    {
        GameObject laser = Instantiate(laserPrefab, transform.position, Quaternion.identity) as GameObject;

        laser.GetComponent<Rigidbody2D>().velocity = new Vector2(0, speed * Time.deltaTime);
    }
}
